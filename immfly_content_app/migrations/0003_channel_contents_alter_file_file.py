# Generated by Django 4.1.7 on 2023-04-04 19:15

from django.db import migrations, models
import immfly_content_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('immfly_content_app', '0002_remove_channel_group_channelgroup_channel_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='contents',
            field=models.ManyToManyField(related_name='channels', to='immfly_content_app.content'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files/', validators=[immfly_content_app.validators.validate_file_extension]),
        ),
    ]