from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="images/%Y/%m/%d", max_length=300)
	content = models.TextField()
	posted_on = models.DateField(auto_now=True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse("blogapp:post_list", kwargs={"pk": self.pk})