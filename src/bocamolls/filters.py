import django_filters
from .models import Bocamoll


class BocamollFilter(django_filters.FilterSet):
    text = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateTimeFilter(lookup_expr='exact')

    class Meta:
        model = Bocamoll
        fields = ['professor', 'subject', 'text', 'date']
