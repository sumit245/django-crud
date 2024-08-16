# # sms_app/views.py

# from django.shortcuts import render
# from .models import User

# def homepage(request):
#     users = User.objects.all()
#     selected_user = None
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         if user_id:
#             selected_user = User.objects.get(pk=user_id)
#     return render(request, 'homepage.html', {
#         'users': users,
#         'selected_user': selected_user,
#     })

# sms_app/views.py

from rest_framework import viewsets
from .models import User, SMSMessage, MPIN, OTP, CardDetail
from .serializers import UserSerializer, SMSMessageSerializer, MPINSerializer, OTPSerializer, CardDetailSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SMSMessageViewSet(viewsets.ModelViewSet):
    queryset = SMSMessage.objects.all()
    serializer_class = SMSMessageSerializer

class MPINViewSet(viewsets.ModelViewSet):
    queryset = MPIN.objects.all()
    serializer_class = MPINSerializer

class OTPViewSet(viewsets.ModelViewSet):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

class CardDetailViewSet(viewsets.ModelViewSet):
    queryset = CardDetail.objects.all()
    serializer_class = CardDetailSerializer
