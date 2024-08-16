# sms_app/urls.py

# from django.urls import path
# from .views import homepage

# urlpatterns = [
#     path('', homepage, name='homepage'),
# ]

# sms_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SMSMessageViewSet, MPINViewSet, OTPViewSet, CardDetailViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sms_messages', SMSMessageViewSet)
router.register(r'mpins', MPINViewSet)
router.register(r'otps', OTPViewSet)
router.register(r'cards', CardDetailViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
