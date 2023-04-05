"""immfly_technical_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from immfly_content_app import views
from immfly_content_app.views import ChannelList, ContentList, SubchannelList, ChannelDetail, ContentDetail


urlpatterns = [
    path('channels/', ChannelList.as_view(), name='channels'),
    path('channels/<int:pk>/', ChannelDetail.as_view(), name='channel-detail'),
    path('channels/<int:channel_id>/subchannels/', SubchannelList.as_view(), name='subchannels'),
    path('channels/<int:channel_id>/contents/', ContentList.as_view(), name='channel_contents'),

    path('contents/', ContentList.as_view(), name='contents'),
    path('contents/<int:pk>/', ContentDetail.as_view(), name='content-detail'),

    

]
