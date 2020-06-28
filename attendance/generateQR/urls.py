from django.urls import path
from . views import generateQRCode

urlpatterns = [
    path('qrcode/', generateQRCode, name='qrcode'),
]