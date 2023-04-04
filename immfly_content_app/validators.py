from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # obtener la extensión del archivo
    valid_extensions = ['.mp4', '.avi', '.pdf', '.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Solo se permiten archivos con extensiones: .mp4, .avi, .pdf, .txt')