# coding: UTF-8
from django.urls import path
from urls_items import views, cbv

app_name = 'urls_items'
urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('new_url/', views.store, name="store"),
    path('urls/', views.index, name="index"),
    path('url-<int:url_id>/', views.edit, name="edit"),
    path(
        'delete-<int:pk>/',
        cbv.UrlDeleteView.as_view(),
        name="delete"
    ),
]