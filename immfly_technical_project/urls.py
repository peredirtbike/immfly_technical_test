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
from immfly_content_app.views import ChannelList, ContentList, SubchannelList, ChannelDetail, ContentDetail, WelcomeView
from rest_framework.schemas import get_schema_view
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Immfly API",
      default_version='v1',
      description="Immfly API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [

    path('', WelcomeView.as_view(), name='welcome'),
    path('channels/', ChannelList.as_view(), name='channels'),
    path('channels/<int:pk>/', ChannelDetail.as_view(), name='channel-detail'),
    path('channels/<int:channel_id>/subchannels/', SubchannelList.as_view(), name='subchannels-list'),
    path('channels/<int:channel_id>/contents/', ContentList.as_view(), name='channel_contents'),

    path('contents/', ContentList.as_view(), name='contents'),
    path('contents/<int:pk>/', ContentDetail.as_view(), name='content-detail'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
