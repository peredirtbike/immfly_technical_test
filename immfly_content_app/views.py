from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Channel, Content
from .serializers import ChannelSerializer, ContentSerializer
from django.views.generic import ListView, DetailView


# Create your views here.



class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel=None)
    serializer_class = ChannelSerializer

class ContentList(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
