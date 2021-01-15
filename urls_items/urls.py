# coding: UTF-8
from django.urls import path
from urls_items import views

app_name = 'urls_items'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
]