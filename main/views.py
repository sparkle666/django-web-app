from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, Person
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import PersonForm, ProfileForm, SignUpForm
from django.contrib.auth import authenticate, login


# Create your views here.
def homepage(request):
	persons = Person.objects.all()
	return render(request=request, template_name="main/home.html", context={"tutorials": Tutorial.objects.all, "persons": persons})
	
def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()	
			login(request, user)
			return redirect("home")
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
	else:
		form = UserCreationForm
	return render(request, "main/register.html", {"form" : form})
	
def logout_request(request):
		logout(request)
		messages.info(request, 'You were logged out.')
		return redirect("/")

def login_request(request):
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
	form = SignUpForm()
	return render(request, "main/login.html", {"form": form})
	
def profile(request):
	if request.method == "POST":
		form = PersonForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/")
	form = PersonForm()
	return render(request, "main/register.html", {"form": form})

def personView(request, ID=1):
	p = Person.objects.get(id=ID)
	st = f"{p.first_name} is {p.id} on the table"
	return HttpResponse(st)
	
def handleform(request):
	if request.method == "POST":	
		form_profile = ProfileForm(request.POST)
		if form_profile.is_valid():
			print(form_profile.cleaned_data['first_name'])
	form_profile = ProfileForm()	
	return render(request, 'main/register.html', {'form': form_profile})