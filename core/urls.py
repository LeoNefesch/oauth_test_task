from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Google OAuth
    path('api/', include('users.urls')),
    path('', lambda request: redirect('account_login')),
]

