from django.db import models
from django.utils.html import format_html
from cloudinary_storage.storage import MediaCloudinaryStorage
import uuid

def cloudinary_folder_path(instance, filename):
    # e.g., photos/abc123.jpg (inside "photos" folder)
    return f'photos/{uuid.uuid4().hex}_{filename}'

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
        storage=MediaCloudinaryStorage(),
        upload_to=cloudinary_folder_path
    )

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="150" height="150" />', self.image.url)
        return "No Image"

    image_tag.short_description = 'Image Preview'
