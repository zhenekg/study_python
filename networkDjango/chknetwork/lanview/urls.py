from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('about/', gate_page, name='gate'),
    path('about/', ats_page, name='ats'),
    path('about/', login_page, name='login')
]
