from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cources/', Cources.as_view(), name='cources'),
    path('cources/<int:pk>', CourceDetail.as_view(), name='cource'),
    path('watch/<int:pk>', VideoDetail.as_view(), name='watch'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
