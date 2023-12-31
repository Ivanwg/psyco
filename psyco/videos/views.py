from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class Cources(LoginRequiredMixin, ListView):
    model = Cource
    queryset = Cource.objects.filter(is_active=True)
    login_url = reverse_lazy('login')
    template_name = 'cources.html'
    context_object_name = 'cources'
    def get_queryset(self):
        return Cource.objects.filter(is_active=True)

class CourceDetail(LoginRequiredMixin, DetailView):
    model = Cource
    template_name = 'cource_detail.html'
    login_url = reverse_lazy('login')
    context_object_name = 'cource'



class VideoDetail(LoginRequiredMixin, DetailView):
    model = Video
    template_name = 'video_watch.html'
    login_url = reverse_lazy('login')
    context_object_name = 'video'
    
class QuizDetail(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quiz.html'
    login_url = reverse_lazy('login')
    context_object_name = 'quiz'

