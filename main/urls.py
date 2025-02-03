from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('delivery-payment/', views.delivery_payment, name='delivery-payment'),
]