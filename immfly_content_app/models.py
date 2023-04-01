from django.db import models

class File(models.Model):
    FILE_CHOICES = (
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('text', 'Text'),
    )
    file = models.FileField(upload_to='files/')
    file_type = models.CharField(max_length=5, choices=FILE_CHOICES)

class Metadata(models.Model):
    description = models.TextField()
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

class Content(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    metadata = models.OneToOneField(Metadata, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

class Group(models.Model):
    name = models.CharField(max_length=50)

class Channel(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    image = models.ImageField(upload_to='channel_images/')
    parent_channel = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subchannels', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def get_all_subchannels(self):
        """
        Returns a queryset of all subchannels of this channel, including their subchannels, and so on.
        """
        subchannels = self.subchannels.all()
        for subchannel in subchannels:
            subchannels |= subchannel.get_all_subchannels()
        return subchannels

    def get_all_contents(self):
        """
        Returns a queryset of all contents of this channel, including the contents of its subchannels, and so on.
        """
        contents = self.contents.all()
        for subchannel in self.get_all_subchannels():
            contents |= subchannel.contents.all()
        return contents

    def get_rating(self):
        """
        Returns the average rating of this channel and its subchannels. If this channel has no contents and no subchannels,
        returns None.
        """
        contents = self.get_all_contents()
        if contents.exists():
            return contents.aggregate(models.Avg('rating'))['rating__avg']
        else:
            return None