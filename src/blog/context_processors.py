from django.contrib.auth.models import User
from .models import Post


def archives(request):
    return {'archives': Post.objects.all(),
            'bocamoll': {'text': 'The quick brown fox jumps over the lazy dog'}}
