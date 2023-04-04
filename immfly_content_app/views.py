from django.shortcuts import render
from rest_framework import generics
from .models import Channel
from .serializers import ChannelSerializer
from django.views.generic import ListView, DetailView


# Create your views here.


class ChannelListView(ListView):
    model = Channel
    template_name = 'channel_list.html'

class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channel_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        channel = self.object
        if channel.subchannels.exists():
            context['subchannels'] = channel.subchannels.all()
        else:
            context['contents'] = channel.contents.all()
        return context