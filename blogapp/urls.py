from django.urls import path
from .views import BlogHome, AddPost, PostList

app_name = "blogapp"
urlpatterns = [
	path("", BlogHome.as_view(), name="blog_home" ),
	path("add/", AddPost.as_view(), name= "add_post"),	
	path("list/<int:pk>/", PostList.as_view(), name="post_list"),
]