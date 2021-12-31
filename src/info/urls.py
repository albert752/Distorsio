from django.urls import path
from .views import HowtotextTemplateView

urlpatterns = [
    path('howtotext', HowtotextTemplateView.as_view(), name='howto-text'),
]
