from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('510ed578-502a-43d3-9ed2-c69e7d2bdacc', views.whatsAppWebhook, name="whatsapp-webhook"),
]


# UUID = 510ed578-502a-43d3-9ed2-c69e7d2bdacc
# Token = 2dc84afb-4bc9-46e3-a750-049bf6cf0483