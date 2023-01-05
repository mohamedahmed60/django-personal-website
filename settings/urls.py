from django.urls import path
from .views import about

app_name = 'settings'
urlpatterns = [
    path('',about),

]