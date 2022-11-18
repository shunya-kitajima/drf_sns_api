from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api_user import serializers
from core.models import Profile, FriendRequest


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


