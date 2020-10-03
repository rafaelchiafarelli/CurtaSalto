from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings as conf_settings
from .models import UniqueLinks, Movie, EmbedddVideo, StartDate, Votes, TempUserID, EmbedddFilm
from .forms import MovieForm, EmbeddedYouTubeForm, VotingForrm, EmbeddedFilmForm
from django.contrib import messages 
from .slots import pages,slot_types,slot_text
import uuid
import datetime
from CurtaSalto.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.core.mail import send_mail  
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
# Create your views here.


def index(request):
    date = StartDate.objects.last()
    embeddedvideo = EmbedddVideo.objects.filter(location = '0').last()
    if 'TempUserID' not in request.session:
        request.session['TempUserID'] = uuid.uuid4().hex
        t_user = TempUserID(user_id=request.session['TempUserID'])
        t_user.save()

    if date is not None:
        lDate = date.LaunchDate.isoformat()
    else:
        lDate = None
    
    slots = dict(slot_types)
    prep = []
    for item in slots:
        prep.append((item,slots[item],slot_text[item]))

    if embeddedvideo is not None:
        eVideo = embeddedvideo.ytLink
    else:
        eVideo = None
    context = {
        'LaunchDate':lDate,
        'ytLink':eVideo,
        'sessions':prep,

    }
    return render(request, 'landpage/index.html', context)

@login_required
def admin(request):
    context = {}
    
    if request.method == 'POST' and "video_form_key" in request.POST:
        print("video found")
        Embedded = EmbeddedYouTubeForm(request.POST)
        if Embedded.is_valid():
            raw_yt_link = Embedded.cleaned_data['ytLink']
            link_dicted = raw_yt_link.split('/')
            if link_dicted is not None:
                yt_part = link_dicted[-1]
            else:
                context = {'error':"link do youtube inválido"}
                return render(request, 'landpage/404.html', context) 
            
            if '=' in yt_part:
                context = {'error':"link do youtube inválido"}
                return render(request, 'landpage/404.html', context) 
            m_obj = EmbedddVideo(tittle = Embedded.cleaned_data['tittle'],
                                synopse = Embedded.cleaned_data['synopse'],
                                category = Embedded.cleaned_data['category'],
                                location = Embedded.cleaned_data['location'],
                                ytLink= yt_part
                                )
            count = EmbedddVideo.objects.filter(location='1').count()

            if count >= 4 and m_obj.location == '1':
                sv = EmbedddVideo.objects.filter(location='1').first().delete()
            m_obj.save()

        return HttpResponseRedirect('/landpage/admin/')
    if request.method == 'POST' and "film_form_key" in request.POST:
        FormFilm = EmbeddedFilmForm(request.POST)
        if FormFilm.is_valid():
            m_obj = EmbedddFilm(**FormFilm.cleaned_data)
            print(m_obj.__str__())
            m_obj.save()
        return HttpResponseRedirect('/landpage/admin/')
    if request.method == 'GET':
        EmbeddedYoutube = EmbeddedYouTubeForm()
        context['video_form'] = EmbeddedYoutube
        EmbeddedFilm = EmbeddedFilmForm()
        context['film_form'] = EmbeddedFilm
    return render(request, 'landpage/admin.html', context)



def webinar(request):

    embeddedvideo = EmbedddVideo.objects.filter(location = '1') 

    if embeddedvideo is not None:
        eVideo = embeddedvideo
    else:
        eVideo = None
    context = {
        'eVideo':eVideo
    }
    return render(request, 'landpage/webnars.html', context)

def awards(request):
    embeddedvideo = EmbedddVideo.objects.filter(location = '3').last()

    if embeddedvideo is not None:
        eVideo = embeddedvideo
    else:
        eVideo = None
    context = {
        'eVideo':eVideo
    }
    return render(request, 'landpage/awards.html', context)




@login_required
def remove(request, content):
    link = UniqueLinks.objects.filter(link=content).first()
    if link is None:
        context = {
            'unique_link':content,
            'fired':True
        }
        return JsonResponse(context)    
    link.fired = False
    link.save()
    host = request.META['HTTP_HOST']
    unique_link = "http://{}/unique_link/{}".format(host,content)
    context = {
        'unique_link':unique_link,
        'fired':False
    }
    return JsonResponse(context)

@login_required
def clean(request, content):
    link = UniqueLinks.objects.filter(link=content).first()
    if link is None:
        context = {
            'unique_link':content,
            'fired':True
        }
        return JsonResponse(context)    
    link.delete()
    host = request.META['HTTP_HOST']
    unique_link = "http://{}/unique_link/{}".format(host,content)
    context = {
        'unique_link':unique_link,
        'deleted':True
    }
    return JsonResponse(context)

@login_required
def begindate(request, content):
    format = '%Y-%m-%d' # The format is 2020-09-30
    datetime_str = datetime.datetime.strptime(content, format) 
    date = StartDate(LaunchDate = datetime_str)
    date.save()
    context = {'registered':True}
    return JsonResponse(context)

@login_required
def generate(request): 
    
    host = request.META['HTTP_HOST']
    access_uuid = uuid.uuid4().hex
    unique_link = "http://{}/landpage/unique_link/{}".format(host,access_uuid)
    obj = UniqueLinks(link = access_uuid)
    obj.save()
    context = {
        "unique_link":unique_link,
    }    
    return JsonResponse(context)

def unique(request, uniq_link):
    
    link = UniqueLinks.objects.filter(link=uniq_link).first()
    if link is None:
        return redirect('index')
    if link.fired is True:
        return redirect('index')
    
    context = {
        'unique_link':uniq_link
    }
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        RegisterForm = MovieForm(request.POST,request.FILES, )
        
        if RegisterForm.is_valid():
            raw_yt_link = RegisterForm.cleaned_data['youtube_link']
            link_dicted = raw_yt_link.split('/')
            if link_dicted is not None:
                yt_part = link_dicted[-1]
            else:
                context = {'error':"link do youtube inválido"}
                return render(request, 'landpage/404.html', context) 
            
            if '=' in yt_part:
                context = {'error':"link do youtube inválido"}
                return render(request, 'landpage/404.html', context) 

            m_obj = Movie(tittle = RegisterForm.cleaned_data['tittle'],
                            synopse = RegisterForm.cleaned_data['synopse'],
                            category = RegisterForm.cleaned_data['category'],
                            email = RegisterForm.cleaned_data['email'],
                            phone = RegisterForm.cleaned_data['phone'],
                            proxy_name = RegisterForm.cleaned_data['proxy_name'],
                            poster_file = RegisterForm.cleaned_data['poster_file'],
                            picture_1 = RegisterForm.cleaned_data['picture_1'],
                            picture_2 = RegisterForm.cleaned_data['picture_2'],
                            picture_3 = RegisterForm.cleaned_data['picture_3'],
                            youtube_link = yt_part,
                            local_display_auth = RegisterForm.cleaned_data['local_display_auth'],
                            social_media_auth = RegisterForm.cleaned_data['social_media_auth'],
                            link=link
                            )
            m_obj.save()
            link.fired = True
            link.save()

            tittle = RegisterForm.cleaned_data['tittle']
            synopse = RegisterForm.cleaned_data['synopse']
            category = RegisterForm.cleaned_data['category']
            email = RegisterForm.cleaned_data['email']
            phone = RegisterForm.cleaned_data['phone']
            proxy_name = RegisterForm.cleaned_data['proxy_name']
            poster_file = RegisterForm.cleaned_data['poster_file']
            picture_1 = RegisterForm.cleaned_data['picture_1']
            picture_2 = RegisterForm.cleaned_data['picture_2']
            picture_3 = RegisterForm.cleaned_data['picture_3']
            youtube_link = RegisterForm.cleaned_data['youtube_link']
            local_display_auth = RegisterForm.cleaned_data['local_display_auth']
            social_media_auth = RegisterForm.cleaned_data['social_media_auth']
            plain_message = "Titulo do filme: {}\r\n Sinopse: {}\r\n Sessão: {}\r\n email: {}\r\n telefone: {}\r\n Nome do responsável: {}\r\n Poster: {}\r\n Foto 1:{}\r\n Foto 2:{}\r\n Foto 3:{}\r\n  Link do Youtube: {} \r\n Autorização para mostrar no site: {}\r\n Autorização para compartilhamento: {} \r\n".format(
                tittle,
                synopse,
                category,
                email,
                phone,
                proxy_name,
                poster_file,
                picture_1,
                picture_2,
                picture_3,
                youtube_link ,
                local_display_auth,
                social_media_auth
            )

            subject = 'CurtaSalto - Obrigado por cadastrar o filme'
            message = plain_message
            recepient = RegisterForm.cleaned_data['email']
            
            
            data = send_mail(subject=subject, 
                message=message,
                from_email=EMAIL_HOST_USER, 
                auth_user= EMAIL_HOST_USER, 
                auth_password = EMAIL_HOST_PASSWORD, 
                recipient_list=[recepient],
                fail_silently = False)
            return redirect('/')
        else:
            context = {'error':"formulário inválido. Tente novamente."}
            return render(request, 'landpage/404.html', context)
    else:
        RegisterForm = MovieForm()
        context['form'] = RegisterForm
    return render(request, 'landpage/register.html', context)


def session(request):

    slots = dict(slot_types)
    prep = []
    for item in slots:
        prep.append((item,slots[item],slot_text[item]))

    context = {
        'sessions':prep,
        
    }
    return render(request, 'landpage/sessions.html', context)

def session_hall(request,selected_hall  ):
    slots = dict(slot_types)
    if str (selected_hall) in slots:
        embbeded_movies = EmbedddFilm.objects.filter(category=selected_hall)
        if embbeded_movies is None:
            context = {
            }
            return render(request,'landpage/404.html',context)            
    else:
        context = {
        }
        return render(request,'landpage/404.html',context)
    movies = []
    for mv in embbeded_movies:
        expiration_date = mv.film.date_posted + datetime.timedelta(days = int(mv.valid_for) )
        if expiration_date > datetime.datetime.now():
            movies.append(mv)
    
    context = {
        'movies':movies,
    }
    return render(request, 'landpage/session_hall.html', context)



def session_detail(request, selected_movie):
    slots = dict(slot_types)
    movie = Movie.objects.get(id=selected_movie)

    if movie is not None:
        form = VotingForrm()
        if 'TempUserID' not in request.session:
            request.session['TempUserID'] = uuid.uuid4().hex
            ThisUser = TempUserID(user_id=request.session['TempUserID'])
            ThisUser.save()
        else:
            ThisUser = TempUserID.objects.get(user_id=request.session['TempUserID'])
        context = {
            'session_name':slots[movie.category],
            'movie':movie,
            'form':form,
            'user':ThisUser,
        }
        return render(request, 'landpage/session_detail.html', context)   
    else:
        context = {
        }
        return render(request,'landpage/404.html',context)


    
    
def vote(request,user, movie_id):
    
    if request.method == "POST":
        json_data = json.loads(json.loads(request.body.decode('utf-8')))
        if 'TempUserID' not in request.session:
            context = {'vote':'fail'}
            return JsonResponse(context)
        else:
            ThisUser = TempUserID.objects.get(user_id=request.session['TempUserID'])
        print(json_data["movie"])
        MovieToVote = Movie.objects.get(pk=int(json_data["movie"]))
        if MovieToVote is not None:
            voted_to = Votes(user_id=ThisUser,vote=MovieToVote)
            voted_to.save()
            context = {'vote':'success'}
        else:
            context = {'vote':'fail'}
        return JsonResponse(context)





































