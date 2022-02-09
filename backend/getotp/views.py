from django.utils import timezone
from drf_yasg.openapi import Schema,TYPE_OBJECT,TYPE_STRING
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN,HTTP_200_OK
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .models import OtpRequest
from .serializers import (request_otp_response_serializer,
                          request_otp_serializer,
                          verify_otp_response_serializer,
                          verify_otp_serializer)

# Create your views here.

class OncePer1MinuteThrottle(UserRateThrottle):
    rate = '1/minute'

class request_otp(APIView):

    throttle_classes = [OncePer1MinuteThrottle]
    @swagger_auto_schema(request_body=Schema(
        type=TYPE_OBJECT,
        properties={
           'phone': Schema(
              type=TYPE_STRING
           )
        }
    )
    )
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
    @swagger_auto_schema(request_body=Schema(
        type=TYPE_OBJECT,
        properties={
           'request_id': Schema(
              type=TYPE_STRING
           ),
           'phone': Schema(
              type=TYPE_STRING
           ),
           'password': Schema(
              type=TYPE_STRING
           )
        }
    )
    )
    def post(self,request):
        serializer=verify_otp_serializer(data=request.data)
        if serializer.is_valid():
            query=OtpRequest.objects.filter(
                request_id=serializer.validated_data['request_id'],
                phone=serializer.validated_data['phone'],
                password=serializer.validated_data['password'],
                valid_until__gte=timezone.now()
                )
            if query.exists():
                User=get_user_model()
                userq = User.objects.filter(username=serializer.validated_data['phone'])
                if userq.exists():
                    user=userq.first()
                    token,created=Token.objects.get_or_create(user=user)
                    return Response(data=verify_otp_response_serializer({'token':token,'new_user':False}).data)

                else:
                    user=User.objects.create(username=serializer.validated_data['phone'])
                    token,created=Token.objects.get_or_create(user=user)
                    return Response(data=verify_otp_response_serializer({'token':token,'new_user':True}).data)
                    
            else:
                return Response(None,status=HTTP_403_FORBIDDEN)

        else:

            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
