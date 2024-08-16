# sms_app/models.py

from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    mobile_number = models.CharField(max_length=15, unique=True, null=False)
    date_of_birth = models.CharField(max_length=40)

    def __str__(self):
        return self.username
        
class MPIN(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mpins')
    mpin = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MPIN for {self.user_profile.username}"

class OTP(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otps')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP for {self.user_profile.username}"

class CardDetail(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Card for {self.user_profile.username}"

class SMSMessage(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=15)
    message = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"SMS from {self.sender} to {self.user_profile.mobile_number} at {self.timestamp}"
