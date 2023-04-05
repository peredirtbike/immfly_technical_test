from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # Obtain the file extension
    valid_extensions = ['.mp4', '.avi', '.pdf', '.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file type. Only files with extensions are allowed: .mp4, .avi, .pdf, .txt')