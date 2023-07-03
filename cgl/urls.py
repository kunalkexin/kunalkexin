'''
from django.urls import path
from pdfshop.views import index, download_pdf

urlpatterns = [
    path('', index, name='index'),
    path('download/', download_pdf, name='download_pdf'),
    
]
'''
from django.urls import include, path

urlpatterns = [
    path('', include('pdfshop.urls')),
]

