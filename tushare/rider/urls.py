from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
app_name = "rider"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
