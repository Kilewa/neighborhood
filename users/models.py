from django.db import models
from django.contrib.auth.models import User
from neighbourhoods.models import Neighbourhood
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    profile_photo = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood, null=True,on_delete=models.CASCADE)

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    def __str__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()      
