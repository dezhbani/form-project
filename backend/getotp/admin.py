from django.contrib import admin
from .models import OtpRequest,User,Profile
# Register your models here.

admin.site.register(OtpRequest)
admin.site.register(User)
admin.site.register(Profile)
