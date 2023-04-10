from rest_framework import serializers
from .models import Channel, Content


class ChannelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        image_url = obj.image.url
        new_image_url = request.build_absolute_uri(image_url.replace('media/', 'media/channel_images/'))
        return new_image_url

    class Meta:
        model = Channel
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

