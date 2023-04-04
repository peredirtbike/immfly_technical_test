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


