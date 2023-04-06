from django.test import TestCase
from immfly_content_app.models import Channel, Content, File, Metadata
from immfly_content_app.validators import validate_file_extension
from unittest.mock import Mock
from django.core.exceptions import ValidationError




class ChannelRatingAlgorithmTestCase(TestCase):
    def setUp(self):        
        self.channel1 = Channel.objects.create(title='Channel 1')
        self.channel2 = Channel.objects.create(title='Channel 2', parent_channel=self.channel1)
        self.channel4 = Channel.objects.create(title='Channel 4')
        self.file1 = File.objects.create(file='test_file.mp4', file_type='video')
        self.file2 = File.objects.create(file='test_file2.mp4', file_type='video')
        self.file3 = File.objects.create(file='test_file3.mp4', file_type='video')
        self.file4 = File.objects.create(file='test_file4.mp4', file_type='video')
        self.metadata1 = Metadata.objects.create(description='Test Description 1', author='Test Author 1', genre='Test Genre 1')
        self.metadata2 = Metadata.objects.create(description='Test Description 2', author='Test Author 2', genre='Test Genre 2')
        self.metadata3 = Metadata.objects.create(description='Test Description 3', author='Test Author 3', genre='Test Genre 3')
        self.metadata4 = Metadata.objects.create(description='Test Description 4', author='Test Author 4', genre='Test Genre 4')
        self.content1 = Content.objects.create(file=self.file1, metadata=self.metadata1, channel=self.channel2, rating=8.5)
        self.content2 = Content.objects.create(file=self.file2, metadata=self.metadata2, channel=self.channel2, rating=6.3)
        self.channel3 = Channel.objects.create(title='Channel 3')
        self.content3 = Content.objects.create(file=self.file3, metadata=self.metadata3, channel=self.channel1, rating=7)
        self.content4 = Content.objects.create(file=self.file4, metadata=self.metadata4, channel=self.channel4, rating=8.0)
        self.file4 = File.objects.create(file='test_file4.sgv', file_type='video')


    def test_channel_rating_with_no_subchannels(self):
        expected_rating = (self.content1.rating + self.content2.rating) / 2
        self.assertAlmostEqual(float(self.channel2.get_rating()), expected_rating, places=5)

    def test_channel_rating_with_subchannels(self):
        expected_rating = (self.content1.rating + self.content2.rating + self.content3.rating) / 3
        self.assertAlmostEqual(float(self.channel1.get_rating()), expected_rating, places=5)

    def test_channel_rating_with_no_contents(self):
        self.assertIsNone(self.channel3.get_rating())

    def test_channel_rating_with_only_one_content(self):
        expected_rating = (self.content4.rating)
        self.assertAlmostEqual(float(self.channel4.get_rating()), expected_rating, places=5)
    
    def test_valid_extension(self):
        mock_file = Mock()
        mock_file.name = 'test_file.mp4'
        try:
            validate_file_extension(mock_file)
        except ValidationError:
            self.fail('validate_file_extension() raised ValidationError unexpectedly.')

    def test_invalid_extension(self):
        mock_file = Mock()
        mock_file.name = 'test_file.docx'
        # Call the validator with the mock file and check that it raises a ValidationError
        with self.assertRaises(ValidationError):
            validate_file_extension(mock_file)