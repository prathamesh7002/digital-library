
from django.contrib import admin
from django.urls import path, include
from E_library import views  # Ensure this import is present

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),  # Ensure this line is present
    path('users/', include('users.urls')),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),  # Ensure this line is present
]