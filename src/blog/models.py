from django.db import models
from django.conf import settings
from uuid import uuid4
from django.utils import timezone
from django.urls import reverse


def change_image_file_name(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/cover/{}.{}'.format(uuid4().hex, ext)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="")
    content = models.TextField()
    cover = models.ImageField(upload_to=change_image_file_name, default='images/cover/default.jpg')
    last_edit_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})