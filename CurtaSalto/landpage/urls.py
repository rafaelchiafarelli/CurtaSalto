from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('admin/', views.admin, name='admin'),
    path('admin/remove/<slug:content>', views.remove, name='remove'),
    path('admin/clean/<slug:content>', views.clean, name='clean'),
    path('admin/begindate/<slug:content>', views.begindate, name='clean'),
    path('admin/generate/', views.generate, name='generate'),
    path('sessions/', views.session, name='session'),
    path('sessions/<int:selected_hall>', views.session_hall, name='session_hall'),
    path('sessions/watch/<int:selected_movie>', views.session_detail, name='session_detail'),
    
    path('webinars/', views.webinar, name='webinar'),
    path('home/', views.index, name='home'),
    path('awards/', views.awards, name='awards'),
    path('unique_link/<slug:uniq_link>', views.unique, name='unique_link'),
    path('vote/<int:movie_id>', views.VotesInMovie, name='voted_group'),
    path('votespermovie/', views.GetVotesGrouped, name='votes_count'),
    path('voted/', views.AllVotes, name='all-voted'),
    path('avg_votes/', views.AvgVotes, name='avg-voted'),
    path('votes/', views.votes, name='votes'),
    path('download_results/', views.download_result, name='download_results'),
    
]

