# coding: UTF-8
from django.urls import path
from urls_items import views, cbv

app_name = 'urls_items'
urlpatterns = [
    path('nouveau/', views.store, name="store"),
    path('', views.index, name="index"),
    path('url-<int:url_id>/', views.edit, name="edit"),
    path('url-detail-<int:url_id>/', views.show, name="show"),
    path(
        'delete-<int:pk>/',
        cbv.UrlDeleteView.as_view(),
        name="delete"
    ),
    path('handle_scan/', views.handle_scan, name="handle_scan"),
]