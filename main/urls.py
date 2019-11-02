from django.urls import path, include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static

app_name="main"
urlpatterns =[
	path("",  homepage, name="home"),
	path("register/", register, name="register"),
	path("logout/", logout_request, name = "logout"),
	path("login/", login_request, name = "login_request"),
	path("profile/", profile, name="profile" ),	path('person/', personView, name="blog"),
	path("person/<int:ID>/", personView, name="blog2" ),
	path("profile/form/", handleform, name= 'profileform')
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)