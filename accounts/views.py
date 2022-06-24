import imp
import re
from django.views.decorators.csrf import csrf_exempt
import email
from unicodedata import name
from django import http
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


from accounts.models import ClientUser
from . import models

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    

@csrf_exempt 
def clientuser(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        client = ClientUser.objects.create(email=email,password=password,status=False,verified=False)
        subject = 'verification link'
        client.save()
        c1 = ClientUser.objects.get(email=email)
        verlink = "http://127.0.0.1:8000/api/verify/"+str(c1.id)
        linebreak = '\n'
        message = f'Please click on the link to verify the account linked to this following email address {email}{linebreak}{verlink}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return http.HttpResponse('Client created')
    return http.HttpResponse()

def verification(request,id):
    client = ClientUser.objects.get(id = id)
    client.verified = True
    client.save()
    return http.HttpResponse(f'Account linked to this email address {client.email} has been verified')

@csrf_exempt
def disable(request):
    if request.method == 'POST':
        # user = serializer.validated_data['user']
        id = request.POST.get('id')
        status = request.POST.get('status')
        client = ClientUser.objects.get(id = id)
        client.status = status
        client.save()
        return http.HttpResponse(f'disabled {client.email}')