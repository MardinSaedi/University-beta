from django.urls import path
from .views import MainPage_view

app_name = "MainPage_urls_name"
urlpatterns = [

    path('', MainPage_view.as_view(), name="MainPage_name"),

]
