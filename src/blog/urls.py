from django.urls import path
from .views import HomeTemplateView, PostDetailView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
