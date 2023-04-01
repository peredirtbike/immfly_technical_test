from django.core.management.base import BaseCommand
from immfly_content_app.models import Channel

import csv

class Command(BaseCommand):
    # This command calculates the ratings of every channel and exports them in a csv file sorted by rating.'

    def handle(self, *args, **options):
        channels = Channel.objects.all()
        ratings = []
        for channel in channels:
            rating = channel.get_rating()
            if rating is not None:
                ratings.append((channel.title, rating))
        ratings.sort(key=lambda x: x[1], reverse=True)
        with open('ratings.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Channel Title', 'Average Rating'])
            for rating in ratings:
                writer.writerow([rating[0], rating[1]])