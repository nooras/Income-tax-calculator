from django.urls import path
from . import views

urlpatterns = [
    path('', views.tax_view ,name="tax_view"),
]

