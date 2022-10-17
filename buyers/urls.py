from django.contrib import admin
from django.urls import path, include
from buyers import views

app_name="buyers"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('buyers/', views.buyers, name='buyers'),
    path('buyers/new/', views.create_buyer, name='new_buyer'),
    path('buyers/<int:buyer_id>/', views.buyer_detail, name='buyer_detail'),
    path('buyers/<int:buyer_id>/edit/', views.buyer_update, name='buyer_update'),
    path('payments/', views.all_payments, name='payments'),
    path('payments/new/', views.create_payment, name='create_payment'),
    path('payments/<int:payment_id>/edit/', views.edit_payment, name='edit_payment'),
    path('payments/<int:payment_id>/delete/', views.delete_payment, name='delete_payment')
]
