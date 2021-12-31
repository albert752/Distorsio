from django.urls import path
from .views import BocamollFilterView, BocamollCreateView

urlpatterns = [
    path('', BocamollFilterView.as_view(), name='bocamoll-filter'),
    path('new', BocamollCreateView.as_view(), name='bocamoll-new'),
]
