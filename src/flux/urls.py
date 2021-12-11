from django.urls import path
from .views import flux

urlpatterns = [
    path('flux', flux, name="flux"),

]