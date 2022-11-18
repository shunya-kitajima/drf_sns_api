from django.db.models import Q
from rest_framework import generics, authentication, permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api_user import serializers
from core.models import Profile, FriendRequest
from core.custompermissions import ProfilePermission


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = serializers.FriendRequestSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(Q(askTo=self.request.user) | Q(askFrom=self.request.user))

    def perform_create(self, serializer):
        try:
            serializer.save(askFrom=self.request.user)
        except:
            raise ValidationError('User can have only unique request')

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'Delete FriendRequest is not arrowed!'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'Patch FriendRequest is not arrowed!'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, ProfilePermission)

    def perform_create(self, serializer):
        serializer.save(userPro=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(userPro=self.request.user)
