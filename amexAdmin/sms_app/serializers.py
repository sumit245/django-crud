# sms_app/serializers.py

from rest_framework import serializers
from .models import User, SMSMessage, MPIN, OTP, CardDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SMSMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSMessage
        fields = '__all__'

class MPINSerializer(serializers.ModelSerializer):
    class Meta:
        model = MPIN
        fields = '__all__'

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'

class CardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetail
        fields = '__all__'
