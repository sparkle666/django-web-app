from django.db import models
from datetime import datetime
from tinymce.widgets import TinyMCE
# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length= 200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField('date published', default=datetime.now())
	
	def __str__(self):
		return self.tutorial_title
		
class Person(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length=200)
	about = models.TextField()
	profile_picture = models.ImageField(upload_to="images/%Y/%m/%d/", max_length=200)
	
	def __str__(self):
		return self.first_name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline