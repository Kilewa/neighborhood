from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Posts,Neighbourhood,Business
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import BusinessForm,PostsForm
from django.contrib.auth.models import User

class HomePage(TemplateView):
    template_name = 'neighbourhoods/index.html'

@login_required
def hoodPage(request):
    hoods = Neighbourhood.objects.all()
    
    return render(request,'neighbourhoods/hoods.html',{"hoods":hoods})

@login_required
def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    businesses = Business.get_profile_businesses(profile.id)

    business_form = BusinessForm(request.POST)
    if request.method == 'POST':
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.location = location
            business.save()
        return redirect('single_hood',location)
    
    else:
        business_form = BusinessForm()
    context = {
        "profile":profile,
        "profile_details":profile_details,
        "businesses":businesses, 
        "business_form":business_form,
    }
    
    return render(request, 'users/profile.html',context) 





@login_required
def single_hood(request,location):

    location = Neighbourhood.objects.get(name=location) 
    print(location.id)
    businesses = Business.get_location_businesses(location.id) 
    posts = Posts.objects.filter(id=location.id) 
    print(posts)

    business_form = BusinessForm(request.POST)
    if request.method == 'POST':
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = request.user
            business.location = location
            business.save()
        return redirect('single_hood',location)
    
    else:
        business_form = BusinessForm()
        
    
    posts_form = PostsForm(request.POST)
    if request.method == 'POST':
        if posts_form.is_valid():
            form = posts_form.save(commit=False)
            form.user = request.user
            form.location = location
            form.save_post()
        return redirect('single_hood',location)
    
    else:
        posts_form = PostsForm()  
        
    context = {"location":location,
                "businesses":businesses,
                "business_form":business_form,
                "posts_form":posts_form,
                "posts":posts,
                }
    
    
    return render(request,'neighbourhoods/hood.html',context)     

