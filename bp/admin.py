from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Videos)
admin.site.register(models.Exercise)
admin.site.register(models.Answers)
