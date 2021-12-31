import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    published_date = django_filters.DateTimeFilter(lookup_expr='exact')


    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'published_date']
