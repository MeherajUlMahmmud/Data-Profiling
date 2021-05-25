from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('EDA', eda_view, name="eda")
]
