from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Posts,Profile,Neighbourhood,Business
from .forms import BusinessForm,PostsForm
from django.contrib.auth.models import User

class HomePage(TemplateView):
    template_name = 'neighbourhoods/index.html'


def index(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'index.html',{"hoods":hoods})

