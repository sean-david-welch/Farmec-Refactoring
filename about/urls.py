from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),

    path('create_model_about/<str:model_name>/', views.create_model_about, name='create_model_about'),
    path('edit_model_about/<str:model_name>/<str:pk>', views.edit_model_about, name='edit_model_about'),
    path('delete_model_about/<str:model_name>/<str:pk>', views.delete_model_about, name='delete_model_about'),
]