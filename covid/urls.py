from django.urls import path
from .views import *

app_name = 'covid'

urlpatterns = [
    path('',reports_display,name='reports_display'),
    path('graphical_display/',graphical_display,name='graphical_display'),
]