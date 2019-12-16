from django.shortcuts import render
from django.http import HttpResponse
from .models import Address, Tutorial
from . import forms 
from adobe_app.forms import NewUserForm

# Create your views here.

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from adobe_app/index.html!"}
#     return render(request,'adobe_app/index.html',context=my_dict)

def index(request):
	return render(request=request,
			template_name="adobe_app/index.html",
			context={"tutorials": Address.objects.all})#, "one_more": Tutorial.objects.all})

def form_name_view(request):
	form = forms.MyNewForm()
	return render(request, 'adobe_app/form_page.html', {"tutorials": Address.objects.all})#{'form':form}, )

# def test(request):
# 	return render(request=request,
# 			template_name="adobe_app/test.html",
# 			context={"one_more": Tutorial.objects.all})

def test2(request):
	return render(request=request,
			template_name="adobe_app/index.html",
			context={"tutorials": Address.objects.all})#, "one_more": Tutorial.objects.all}


def test(request):
	return render(request=request,
			template_name="adobe_app/index.html",
			context={"tutorials": Address.objects.all})#, "one_more": Tutorial.objects.all})python


def users(request):
	form = NewUserForm()
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR FORM INVALID")
	return render(request, 'adobe_app/users.html', {'form':form})

