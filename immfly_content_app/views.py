from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Channel, Content
from .serializers import ChannelSerializer, ContentSerializer
from django.http import HttpResponse




class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel=None)
    serializer_class = ChannelSerializer

class ChannelDetail(generics.RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class SubchannelList(generics.ListAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        channel_id = self.kwargs['channel_id']
        channel = Channel.objects.get(id=channel_id)
        return channel.get_all_subchannels()


class ContentList(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        if channel_id:
            channel = Channel.objects.get(id=channel_id)
            return channel.get_all_contents()
        else:
            return Content.objects.all()

class ContentDetail(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
