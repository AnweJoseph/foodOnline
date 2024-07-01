import os
from django.core.exceptions import ValidationError

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1] #  cover-image.jpg, .png, .jpeg

    valid_extenstions = ['.png', '.jpg', '.jpeg']
    if not ext.lower in valid_extenstions:
        raise ValidationError('Unsupported file extensions. Allowed extensions: ' + str(valid_extenstions))
    