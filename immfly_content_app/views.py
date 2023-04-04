from django.shortcuts import render
from rest_framework import generics
from .models import Channel
from .models import Content
from .models import Metadata
from .models import File
from .serializers import ChannelSerializer
from .serializers import ContentSerializer
from .serializers import MetadataSerializer
from .serializers import FileSerializer
# Create your views here.


class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel__isnull=True)
    serializer_class = ChannelSerializer

class SubchannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel__isnull=False)
    serializer_class = ChannelSerializer

class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class MetadataList(generics.ListAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class FileList(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
