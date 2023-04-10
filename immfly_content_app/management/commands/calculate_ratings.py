from django.core.management.base import BaseCommand
from immfly_content_app.models import Channel
import os
import csv

class Command(BaseCommand):
    # This command calculates the ratings of every channel and exports them in a csv file sorted by rating.

    def handle(self, *args, **options):
        # Get all channels from the database
        channels = Channel.objects.all()
        # Create a list to store the channel ratings
        ratings = []
        # Iterate over each channel and calculate its rating
        for channel in channels:
            rating = channel.get_rating()
            # Add the channel title and rating to the list if the rating is not None
            if rating is not None:
                ratings.append((channel.title, round(rating, 2)))
        # Sort the ratings list by rating in descending order
        ratings.sort(key=lambda x: x[1], reverse=True)
        # Write the ratings to a CSV file
        with open('ratings.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Channel Title', 'Average Rating'])
            for rating in ratings:
                writer.writerow([rating[0], rating[1]])
        # Print the current working directory to confirm the location of the CSV file
        print(os.getcwd())