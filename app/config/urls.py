"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


from . import views
from members.apis import AuthTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api/login/', AuthTokenView.as_view()),
    path('api/address/', include('address.urls')),
    path('api/banner/', include('banners.urls')),
    path('api/member/', include('members.urls')),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/order/', include('order.urls')),
    path('api/direction/', views.static_directions),
]
