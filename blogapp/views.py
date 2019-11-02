from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import BlogPost
from django.urls import reverse_lazy

#from django.urls import reverse
# Create your views here.

class BlogHome(TemplateView):
	template_name = "blogapp/home.html"

class AddPost(CreateView):	
	#template_name="blogapp/blogpost_form.html"
	fields = ["title", "image", "content"]
	model = BlogPost
	success_url = reverse_lazy("blogapp:blog_home")
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
			
class PostList(ListView):
	model = BlogPost
	context_object_name = "post_list"			