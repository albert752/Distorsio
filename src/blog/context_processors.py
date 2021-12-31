from .models import Category, Post


def categories(request):
    return {'categories': Category.objects.all()}


def archives(request):
    return {'archives': Post.objects.all(),
            'bocamoll': {'text': 'The quick brown fox jumps over the lazy dog'}}
