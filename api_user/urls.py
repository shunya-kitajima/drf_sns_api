from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_user import views

app_name = 'user'

router = DefaultRouter()
router.register('approval', views.FriendRequestViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
]
