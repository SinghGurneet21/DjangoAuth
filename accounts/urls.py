from django import views
from .views import RegisterAPI, LoginAPI, clientuser, verification, disable, clientlogin, clientlogout
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/signup/', clientuser, name='signup'),
    path('api/verify/<int:id>', verification, name='verify'),
    path('api/disable/', disable, name='disable'),
    path('api/client/login', clientlogin, name='clientlogin'),
    path('api/client/logout', clientlogout, name='clientlogout'),
]