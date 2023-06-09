# Generated by Django 4.1.7 on 2023-04-04 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('immfly_content_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='group',
        ),
        migrations.CreateModel(
            name='ChannelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immfly_content_app.channel')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='immfly_content_app.group')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='group',
            field=models.ManyToManyField(to='immfly_content_app.group'),
        ),
    ]
