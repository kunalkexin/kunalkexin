from django.urls import path
from . import views
from pdfshop.views import index, download_pdf

app_name = 'pdfshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),

    path('create-order/', views.create_order, name='create_order'),

    path('payment-success/', views.payment_success, name='payment_success'),
    
    path('webhook/', views.webhook_view, name='webhook'),
    
    
]
