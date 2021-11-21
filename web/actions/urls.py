from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views



app_name = 'actions'

router = DefaultRouter()
router.register('followers', views.ListFollowerViewSet, basename='followers')


urlpatterns = [
    path('followers/<to_user_id>/', views.FollowerViewSet.as_view({'get': 'list'}), name='followers_to_user'),
    path('subscription/', views.FollowerViewSet.as_view({'post': 'create'}), name='subscriber_to_user'),
    path('user/followers/', views.FollowerViewSet.as_view({'get': 'user_followers'}), name='user_followers'),
    path('user/following/', views.FollowerViewSet.as_view({'get': 'user_following'}), name='user_following'),

]
urlpatterns += router.urls
