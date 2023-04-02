import os
from django.apps import AppConfig
from django.conf import settings



class ImmflyContentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'immfly_content_app'
    

    def ready(self):
        # create the directories if they don't exist
        media_root = settings.MEDIA_ROOT
        files_dir = os.path.join(media_root, 'files')
        channel_images_dir = os.path.join(media_root, 'channel_images')
        os.makedirs(files_dir, exist_ok=True)
        os.makedirs(channel_images_dir, exist_ok=True)