from django.contrib import admin

from .models import *
from users.models import Profile

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Posts)