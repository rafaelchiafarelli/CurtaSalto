from django.contrib import admin
from .models import UniqueLinks, Movie, EmbedddVideo, StartDate, Votes, TempUserID, EmbedddFilm
# Register your models here.
admin.site.register(UniqueLinks)
admin.site.register(Movie)
admin.site.register(EmbedddVideo)
admin.site.register(Votes)
admin.site.register(TempUserID)
admin.site.register(EmbedddFilm)