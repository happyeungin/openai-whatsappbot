from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('123', views.whatsAppWebhook, name="whatsapp-webhook"),
]