from django.urls import path
from .views import *

urlpatterns = [
    path('',reports_display,name='reports_display'),
]