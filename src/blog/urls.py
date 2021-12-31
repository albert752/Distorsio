from django.urls import path
from .views import HomeTemplateView, PostDetailView, PostFilterView, CategoryDetailView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('post', PostFilterView.as_view(), name='post-filter'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
]
