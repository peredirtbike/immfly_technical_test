from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Channel, Content
from .serializers import ChannelSerializer, ContentSerializer
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from drf_yasg import openapi





class WelcomeView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns a welcome message",
        responses={200: openapi.Response(description="Welcome message", schema=openapi.Schema(type="object", properties={"message": openapi.Schema(type="string")}))}
    )
    def get(self, request):
        message = {'message': 'Welcome to my API! Read the documentation on /docs to get success!'}
        return Response(message)
        

class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.filter(parent_channel=None)
    serializer_class = ChannelSerializer

    @swagger_auto_schema(
        operation_description="List of channels",
        operation_summary="Returns a list of channels",
        responses={200: ChannelSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ChannelDetail(generics.RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    @swagger_auto_schema(
        operation_summary="Retrieve a single channel",
        operation_description="Retrieve a single channel instance by specifying its ID in the URL.",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=ChannelSerializer()
            ),
            404: "Channel not found",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubchannelList(generics.ListAPIView):
    serializer_class = ChannelSerializer


    def get_queryset(self):
        channel_id = self.kwargs['channel_id']
        channel = Channel.objects.get(id=channel_id)
        return channel.get_all_subchannels()
    
    @swagger_auto_schema(
        operation_summary="List subchannels",
        operation_description="List all subchannels of a parent channel.",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=ChannelSerializer(many=True)
            ),
            404: "Parent channel not found",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class ContentList(generics.ListAPIView):
    serializer_class = ContentSerializer

    @swagger_auto_schema(
        operation_description="List of contents",
        operation_summary="Returns a list of contents",
        responses={200: ContentSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

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
    @swagger_auto_schema(
        operation_summary="Retrieve a single content",
        operation_description="Retrieve a single content instance by specifying its ID in the URL.",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=ContentSerializer()
            ),
            404: "Content not found",
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
