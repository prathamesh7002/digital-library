
from django.contrib import admin
from django.urls import path, include
from E_library import views  # Ensure this import is present
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),  # Ensure this line is present
    path('users/', include('users.urls')),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('library/', include('library.urls')),  # Ensure this line is present
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)