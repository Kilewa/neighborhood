from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.HomePage.as_view(),name='home'),
]
