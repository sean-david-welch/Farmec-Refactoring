from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.suppliers, name='suppliers'),
    path('supplier/<str:pk>', views.supplier_page, name='supplier'),

    path('create_model_supplier/<str:model_name>/', views.create_model_supplier, name='create_model_supplier'),
    path('edit_model_supplier/<str:model_name>/<str:pk>', views.edit_model_supplier, name='edit_model_supplier'),
    path('delete_model_supplier/<str:model_name>/<str:pk>', views.delete_model_supplier, name='delete_model_supplier'),
]