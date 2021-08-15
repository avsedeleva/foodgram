from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.utils import timezone
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import User
from djoser import views

