from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]
