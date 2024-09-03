"""
URL configuration for CarRental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from  car import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls')),
    path('car/<id>', views.id),
    path('home/', views.home),
    path('home/<id>', views.id),
    path('about/', views.about),
    path('about/<id>',views.id),
    path('auto/', views.auto),
    path('auto/<id>', views.id),
    path('bicycle/', views.bicycle),
    path('bicycle/<id>', views.id),
    path('bmw/', views.bmw),
    path('bmw/<id>', views.id),
    path('bolero/', views.bolero),
    path('bolero/<id>', views.id),
    path('cars/', views.cars),
    path('cars/<id>', views.id),
    path('checkout/', views.checkout),
    path('checkout/<id>', views.id),
    path('jeep/', views.jeep),
    path('jeep/<id>', views.id),
    path('lambo/', views.lambo),
    path('lambo/<id>', views.id),
    path('lambo2/', views.lambo2),
    path('lambo2/<id>', views.id),
    path('merc/', views.merc),
    path('merc/<id>', views.id),
    path('pricing/', views.pricing),
    path('pricing/<id>', views.id),
    path('sign/', views.sign),
    path('sign/<id>', views.id),
    path('login/', views.login),
    path('login/<id>', views.id),
    path('registered/', views.registered),
    path('registered/<id>', views.id),
    path('dashboard/', views.dashboard),
    path('dashboard/<id>', views.id),
    path('bike/', include('bike.urls')),
    path('bicycle/', include('bicycle.urls'))
]
