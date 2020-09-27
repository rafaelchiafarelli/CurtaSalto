from django.db import models
from django.utils import timezone
from .slots import pages, slot_types, grades
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class UniqueLinks(models.Model):
    link = models.CharField(max_length=100)
    fired = models.BooleanField(blank=False,null=False,default=False)


class Movie(models.Model):
    tittle = models.CharField(max_length=100,blank = False, null = False)
    synopse = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.CharField(choices=slot_types,max_length=100,blank = False, null = False)
    email =  models.EmailField(max_length=254, blank = False, null = False)
    phone = PhoneNumberField(max_length=100,blank = False, null = False)
    proxy_name = models.CharField(max_length=100,blank = False, null = False)
    poster_file = models.FileField(upload_to='uploads/poster_file')
    picture_1= models.FileField(upload_to='uploads/picture_1',blank = True, null = True)
    picture_2= models.FileField(upload_to='uploads/picture_2',blank = True, null = True)
    picture_3= models.FileField(upload_to='uploads/picture_3',blank = True, null = True)
    youtube_link =  models.CharField(max_length=200,blank = False, null = False)
    local_display_auth = models.BooleanField(blank = False, null = False)
    social_media_auth  = models.BooleanField(blank = False, null = False)
    link = models.ForeignKey(UniqueLinks, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle
#https://www.youtube.com/watch?v=YIm7KBIwy94
class EmbedddVideo(models.Model):
    tittle = models.CharField(max_length=100,blank = True, null = True)
    ytLink = models.CharField(max_length=200,blank = False, null = False)
    location = models.CharField(choices=pages,max_length=25,blank = True, null = True)
    synopse = models.TextField(blank = True, null = True)
    category = models.CharField(choices=slot_types,max_length=100,blank = True, null = True)


class StartDate(models.Model):
    LaunchDate = models.DateTimeField(blank = True, null = True)

class TempUserID(models.Model):
    user_id = models.CharField(max_length=50,blank=False,null=False)

class Votes(models.Model):
    user_id = models.ForeignKey(TempUserID, on_delete=models.CASCADE)
    vote = models.ForeignKey(Movie, on_delete=models.CASCADE)
    photografy = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    art_design = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    picture = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    acting = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    sound_desing = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    adaptation = models.CharField(choices=grades,max_length=100,blank = False, null = False, default='0')
    


