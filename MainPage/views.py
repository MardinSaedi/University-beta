from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

# Create your views here.
class MainPage_view(TemplateView):
    template_name = "MainPage/index.html"
