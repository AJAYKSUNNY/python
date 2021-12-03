from django.urls import path
from .views import getReport

urlpatterns = [
    path('report/',getReport ),
]