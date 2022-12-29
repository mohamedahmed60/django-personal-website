from django.db import models

# Create your models here.
class About(models.Model):
    blog_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    subtitle = models.TextField(max_length=500)
    aboutme = models.TextField(max_length=1000)
    tw_link = models.URLField()
    tk_in_link = models.URLField()
    github_link = models.URLField()