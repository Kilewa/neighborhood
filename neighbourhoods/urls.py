from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.HomePage.as_view(),name='home'),
    url('^hoods/',views.hoodPage,name='hoodPage'),  
    url(r'^hood/(?P<location>\w+)',views.single_hood,name='single_hood'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]
