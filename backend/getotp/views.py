from datetime import datetime
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST,HTTP_403_FORBIDDEN
from rest_framework.views import APIView
from .models import OtpRequest
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.throttling import UserRateThrottle
from .serializers import (
    request_otp_serializer,
    request_otp_response_serializer,
    verify_otp_serializer,
    verify_otp_response_serializer,
    )
# Create your views here.

class OncePer2MinuteThrottle(UserRateThrottle):
    rate = '2/minute'

class request_otp(APIView):

    # throttle_classes = [OncePer2MinuteThrottle]

    def post(self,request):
        serializer = request_otp_serializer(data=request.data)
        if serializer.is_valid():
            otp = OtpRequest()
            otp.phone = serializer.validated_data['phone']
            otp.generate_password()
            otp.save()

            #send sms


            return Response(request_otp_response_serializer(otp).data)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



class verify_otp(APIView):
    def post(self,request):
        serializer=verify_otp_serializer(data=request.data)
        if serializer.is_valid():
            query=OtpRequest.objects.filter(
                request_id=serializer.validated_data['request_id'],
                phone=serializer.validated_data['phone'],
                password=serializer.validated_data['password'],
                valid_until__gte = datetime.now(),
                )
            if query.exists():
                User=get_user_model()
                userq = User.objects.filter(username=serializer.validated_data['phone'])
                if userq.exists():
                    user=userq.first()
                    token,created=Token.objects.get_or_create(user=user)
                    return Response(data=verify_otp_response_serializer(data={'token':token,'new_user':False}).data)

                else:
                    user=User.objects.create(username=serializer.validated_data['phone'])
                    token,created=Token.objects.get_or_create(user=user)
                    return Response(data=verify_otp_response_serializer(data={'token':token,'new_user':True}).data)
                    
            else:
                print("inja1")
                return Response(None,status=HTTP_403_FORBIDDEN)

        else:
            print("inja2")

            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
