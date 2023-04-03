from django.shortcuts import render
from rest_framework import generics
from .models import Channel
from .models import Content
from .serializers import ChannelSerializer
from .serializers import ContentSerializer
# Create your views here.


class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel=None)
    serializer_class = ChannelSerializer

class SubchannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel__isnull=False)
    serializer_class = ChannelSerializer

class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
