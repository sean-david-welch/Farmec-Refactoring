from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs'),
    path('blog/<str:pk>/', views.single_blog, name='single_blog'),

    path('exhibitions/', views.exhibitions, name='exhibitions'),

    path('create_model_blog/<str:model_name>/', views.create_model_blog, name='create_model_blog'),
    path('update_model_blog/<str:model_name>/<str:pk>/', views.edit_model_blog, name='edit_model_blog'),
    path('delete_model_blog/<str:model_name>/<str:pk>/', views.delete_model_blog, name='delete_model_blog'),
]
