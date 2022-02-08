from rest_framework import serializers
from .models import OtpRequest
class request_otp_serializer(serializers.Serializer):
    phone=serializers.CharField(max_length=14,allow_null=False)

class request_otp_response_serializer(serializers.ModelSerializer):
    class Meta:
        model = OtpRequest
        fields=['request_id']


class verify_otp_serializer(serializers.Serializer):
    request_id=serializers.CharField(max_length=64,allow_null=False)
    phone=serializers.CharField(max_length=14,allow_null=False)
    password=serializers.CharField(allow_null=False)


class verify_otp_response_serializer(serializers.Serializer):
    token=serializers.CharField()
    new_user=serializers.BooleanField()