"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from bugtracker.views import dashboard, profile
from django.contrib import admin
from django.urls import path
import os
from django.urls.conf import include
from api import urls as api_urls
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls), name='api'),
    path('tickets/', include('tickets.urls')),
    path('accounts/',
        include(('django.contrib.auth.urls', 'auth'),
        namespace='accounts')
    ),
    path('dashboard', dashboard, name='dashboard'),
    path('accounts/profile/', profile, name='profile'),
]

# if in developemnt mode
if os.environ.get('DJANGO_CONFIGURATION') == 'Dev':
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))