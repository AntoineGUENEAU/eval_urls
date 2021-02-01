from django.urls import path
from urls_results import views

app_name = 'urls_results'
urlpatterns = [
    path('delete-<int:result_id>/', views.delete, name="delete"),
]