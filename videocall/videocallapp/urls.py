from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from videocallapp.views import UserViewSet, HeroViewSet, api_root
from rest_framework import renderers

hero_list = HeroViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
hero_detail = HeroViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns=format_suffix_patterns([
	path('hero/<int:pk>/', hero_detail, name='hero-detail'),
	path('users/<int:pk>/', user_detail, name='user-detail'),
	path('hero/', hero_list, name='hero-list'),
	path('users/', user_list, name='user-list'),
	path('', api_root),
])