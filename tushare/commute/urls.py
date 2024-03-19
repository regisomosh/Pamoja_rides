from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

appname = 'commute'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('get-a-quote/', GetaquoteView.as_view(), name='get-a-quote'),
    path('sample-inner-page/', SampleinnerpageView.as_view(), name='sample-inner-page'),
    path('service-details/', ServicedetailsView.as_view(), name='services'),
   

    path('user_type_selection/', UserTypeSelectionView.as_view(), name='user_type_selection'),
]
