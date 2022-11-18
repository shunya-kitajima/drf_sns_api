from django.db.models import Q
from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api_dm import serializers
from core.models import Message


