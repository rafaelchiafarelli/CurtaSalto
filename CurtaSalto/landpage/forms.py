from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, EmbedddVideo, Votes, EmbedddFilm
from phonenumber_field.formfields import PhoneNumberField

class MovieForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'autocomplete': 'on',
        'class': 'form-control',
        'placeholder': 'seuemail@email.com',
        'required': 'obrigatório'
        }),error_messages={'invalid': 'email inválido, tente novamente'},required = True)

    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': "+5511991386776"}), 

                       label=("Telefone"), error_messages={'invalid': 'email inválido, tente novamente'},required=True)
    class Meta:
        model = Movie
        fields = ['tittle',
                'synopse',
                'category',
                'participants',
                'email',
                'phone',
                'proxy_name',
                'poster_file',
                'picture_1',
                'picture_2',
                'picture_3',
                'youtube_link',
                'local_display_auth',
                'social_media_auth'
                ]

        labels = {
                'tittle':'Titulo',
                'synopse':'Sinopse',
                'category':'Mostra',
                'participants':'Participantes',
                'email':'email',
                'phone':'Telefone',
                'proxy_name':'Responsável',
                'poster_file':'Poster (vertical)',
                'picture_1':'Foto promocional',
                'picture_2':'Foto promocional',
                'picture_3':'Foto promocional',
                'youtube_link':'Link de acesso',
                'local_display_auth':'Permite mostrar o filme nesse site',
                'social_media_auth':'Permite que o filme seja mostrado nas mídias sociais',
        }
        help_texts = {
                'tittle':'Titulo do filme',
                'synopse':'Sinopse do filme',
                'category':'Mostra',
                'participants':'Estudantes participantes',
                'email':'email',
                'phone':'telefone (WhatsApp)',
                'proxy_name':'Nome do responsável',
                'poster_file':'Poster do filme (vertical)',
                'picture_1':'Foto promocional do filme (horizontal)',
                'picture_2':'Foto promocional do filme (horizontal)',
                'picture_3':'Foto promocional do filme (horizontal)',
                'youtube_link':'Link do youtube (não listado ou público)',
                'local_display_auth':'Permite mostrar o filme nesse site',
                'social_media_auth':'Permite que o filme seja mostrado nas mídias sociais',        
                }
        error_messages = {
                'tittle':{'required': 'Obrigatório'},
                'synopse':{'required': 'Obrigatório'},
                'category':{'required': 'Obrigatório'},
                'participants':{'required':'Obrigatório'},
                'email':{'required': 'Obrigatório'},
                'phone':{'required': 'Obrigatório'},
                'proxy_name':{'required': 'Obrigatório'},
                'poster_file':{'required': 'Obrigatório'},
                'picture_1':{'required': 'Obrigatório'},
                'picture_2':{'required': 'Obrigatório'},
                'picture_3':{'required': 'Obrigatório'},
                'youtube_link':{'required': 'Obrigatório'},
                'local_display_auth':{'required': 'Obrigatório'},
                'social_media_auth':{'required': 'Obrigatório'},
                }
    

class EmbeddedYouTubeForm(ModelForm):
    
    class Meta:
        model = EmbedddVideo
        fields = [
                'tittle',
                'synopse',
                'category',
                'ytLink',
                'location'
                ]
        labels = {
                'tittle':'Titulo',
                'synopse':'Synopse',
                'category':'Mostra',
                'ytLink':'Link',
                'location':'Local'
                

        }
        help_texts = {
                'tittle':'Titulo do vídeo',
                'synopse':'Sinopse do conteúdo',
                'category':'Mostra',
                'ytLink':'Link para o vídeo no youtube',
                'location':'Local aonde será mostrado esse vídeo'
                }
        error_messages = {
                'tittle':{'required': 'Obrigatório'},
                'synopse':{'required': 'Obrigatório'},
                'category':{'required': 'Obrigatório'},
                'ytLink':{'required': 'Obrigatório'},
                'location':{'required': 'Obrigatório'}
                }

class EmbeddedFilmForm(ModelForm):
        class Meta:
                model = EmbedddFilm
                fields = [
                        'film',
                        'category',
                        'valid_for'
                        ]
                labels = {
                        'film':'Selecione o filme',
                        'category':'Tipo de mostra',
                        'valid_for':'Dias de exibição'

                }
                help_texts = {
                        'film':'',
                        'category':'Mostra',
                        'valid_for':'Ficará exposto durante essa quantidade de dias'

                        }
                error_messages = {
                        'film':{'required': 'Obrigatório'},
                        'category':{'required': 'Obrigatório'},
                        'valid_for':{'required':'Obrigatório'}
                        }
        film = forms.ModelChoiceField(queryset=Movie.objects.all())


class VotingForrm(ModelForm):

    class Meta:
        model = Votes
        fields = [
		'general_score']
        labels = {
                'general_score':'Nota do Filme'
        }
