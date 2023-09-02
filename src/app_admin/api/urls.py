from django.urls import path

from .views import *

app_name = 'app_admin'
urlpatterns = [
    # login
    path('login/', AdminLoginView.as_view(), name='admin_login'),
]
