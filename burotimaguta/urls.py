"""burotimaguta URL Configuration

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
from django.contrib import admin
from django.urls import path
from buyers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('buyers/', views.buyers, name='buyers'),
    path('buyers/new/', views.create_buyer, name='new_buyer'),
    path('buyers/<int:buyer_id>/', views.buyer_detail, name='buyer_detail'),
    path('buyers/<int:buyer_id>/edit/', views.buyer_update, name='buyer_update'),
    path('payments/', views.all_alllowances, name='payments'),
    path('payments/new/', views.create_payment, name='create_payment'),
    path('payments/<int:payment_id>/edit/', views.edit_payment, name='edit_payment'),
    path('payments/<int:payment_id>/delete/', views.delete_payment, name='delete_payment')
]
