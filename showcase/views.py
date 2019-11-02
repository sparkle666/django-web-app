from django.shortcuts import render, redirect
from .forms import DesignForm, DesignCategoryForm, LoginForm
from .models import Design, DesignCategory	
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_home(request):
	category_list = DesignCategory.objects.all()
	return render(request, "showcase/home.html", {"category_list": category_list})

@login_required(login_url= "/showcase/login/")
def add_pic(request):
	if request.method == "POST":
		form = DesignForm(request.POST, request.FILES)
		if form.is_valid():
			like = form.save()
			messages.success(request, "Suucessfully added!!")
			return redirect("showcase:show_home")
	form = DesignForm()
	return render(request, "showcase/add_pic.html", {"form": form})

def login_show(request):		
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username= username, password= password)
			if user is not None:
				login(request, user)
				return redirect("/showcase/")
	else:
		form = LoginForm()
	return render(request, "showcase/login.html", {"form" : form})
	
def logout_show(request):
	logout(request)
	return redirect("showcase:show_home")

@login_required(login_url="/showcase/login/")		
def add_category(request):
	if request.method == "POST":
		form = DesignCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Category added successfully!!")
			return redirect("/showcase/")
	else:	
	   	form = DesignCategoryForm
	return render(request, "showcase/login.html", {"form": form})

def category_list(request, category_name):
	list_in_category = Design.objects.filter(design_category__name= category_name)
	return render(request, "showcase/list.html", {"list_in_category": list_in_category})

def like_design(request, id):
	liked_design = Design.objects.get(id=id)
	# If the number of like in db is null then make a variable and set it to 0, then imcrement it.
	if liked_design.likes is None:
		user_like = 0
		user_like +=1
		liked_design.likes = user_like
	else:
		# if the model like variable ie integer then get that integer and increment it. 
		user_like = int(liked_design.likes)
		user_like += 1
		liked_design.likes = user_like
	liked_design.save()
	return redirect(reverse("showcase:category_list", args = [str(liked_design.design_category.name)]))