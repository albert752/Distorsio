from django_filters.views import FilterView
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Bocamoll
from .filters import BocamollFilter
from django.urls import reverse_lazy


class BocamollFilterView(FilterView):
    model = Bocamoll
    filterset_class = BocamollFilter
    ordering = ['-creation']
    paginate_by = 10

    def get_queryset(self):
        return super(BocamollFilterView, self).get_queryset().filter(approved=True)


class BocamollCreateView(SuccessMessageMixin, CreateView):
    model = Bocamoll
    fields = ['professor', 'subject', 'date', 'text']
    success_url = reverse_lazy('bocamoll-new')
    success_message = "El bocamoll ha estat enviat a revisió!"
