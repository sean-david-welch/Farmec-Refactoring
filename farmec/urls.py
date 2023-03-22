from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),

    path('home', include('home.urls')),
    path('about/', include('about.urls')),    
    path('suppliers/', include('suppliers.urls')),
    path('spareparts/', include('spareparts.urls')),
    path('payments/', include('payments.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)