from django.urls import path, include
from showcase.views import *

app_name = "showcase"
urlpatterns = [
		path("", show_home, name="show_home"),
		path("add/pic/", add_pic, name="add_pic"),
		path("login/", login_show, name="showlogin"),
		path("logout/", logout_show, name=" showlogout"),
		path("add/category/", add_category, name="add_category"),
		path('all/category/<str:category_name>/', category_list, name='category_list'),
		path("like/design/<int:id>/", like_design, name="like_design"),
]