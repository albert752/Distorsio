from django.db import models
from django.conf import settings
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse
from PIL import Image


def change_image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/cover/{}.{}'.format(uuid4().hex, ext)


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='categoria')
    description = models.TextField(verbose_name='descripció')

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='autor')
    title = models.CharField(max_length=200, verbose_name='títol')
    subtitle = models.CharField(max_length=200, default="", verbose_name='subtitol')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='categoria')
    content = models.TextField(verbose_name='contingut')
    cover = models.ImageField(upload_to=change_image_file_name, default='images/cover/default.jpg')
    last_edit_date = models.DateTimeField(default=timezone.now, verbose_name='última edició')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='data de publicació')

    @property
    def thumbnail(self):
        file_name = self.cover.url.split('/')[-1]
        return self.cover.url.replace(file_name, f'thumb-{file_name}')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cover.path)
        thumbnail_output_size = (200, 250)
        crop_width, crop_height = thumbnail_output_size
        width, height = img.size

        left = (width - crop_width) / 2
        top = (height - crop_height) / 2
        right = (width + crop_width) / 2
        bottom = (height + crop_height) / 2
        img = img.crop((left, top, right, bottom))
        img.thumbnail(thumbnail_output_size)
        file_name = self.cover.path.split('/')[-1]
        thumbnail_path = self.cover.path.replace(file_name, f'thumb-{file_name}')
        img.save(thumbnail_path)
