from abc import update_abstractmethods
from pyexpat import model
from turtle import title
from django.db import models


class Video(models.Model):
    title = models.CharField()
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    video_id =  models.CharField()
    # update_at 
    # state 
    # publish_at