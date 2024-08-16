# sms_app/admin.py

from django.contrib import admin
from .models import User, SMSMessage, MPIN, OTP, CardDetail

class SMSMessageInline(admin.TabularInline):
    model = SMSMessage
    extra = 0

class MPINInline(admin.TabularInline):
    model = MPIN
    extra = 0

class OTPInline(admin.TabularInline):
    model = OTP
    extra = 0

class CardDetailInline(admin.TabularInline):
    model = CardDetail
    extra = 0

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile_number', 'date_of_birth')
    inlines = [MPINInline, OTPInline, CardDetailInline, SMSMessageInline]

@admin.register(SMSMessage)
class SMSMessageAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'sender', 'timestamp')
    search_fields = ('user_profile__username', 'sender')

@admin.register(MPIN)
class MPINAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'mpin', 'created_at')
    search_fields = ('user_profile__username',)

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'otp', 'created_at')
    search_fields = ('user_profile__username',)

@admin.register(CardDetail)
class CardDetailAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'card_number', 'expiry_date')
    search_fields = ('user_profile__username',)
