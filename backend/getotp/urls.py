from django.urls import path
from .views import request_otp,verify_otp

urlpatterns = [
    path("request/",request_otp.as_view()),
    path("verify/",verify_otp.as_view()),
]
