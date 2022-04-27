from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.getData),
    path('',views.home_view),
]