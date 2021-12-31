from django.views.generic import ListView, DetailView, TemplateView
from django_filters.views import FilterView
from .models import Post, Category
from .filters import PostFilter


class HomeTemplateView(ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context['featured_main'] = context['object_list'][len(context['object_list'])-1]
        context['featured_left'] = context['object_list'][len(context['object_list'])-2]
        context['featured_right'] = context['object_list'][len(context['object_list'])-3]
        return context


class PostDetailView(DetailView):
    model = Post


class PostFilterView(FilterView):
    model = Post
    filterset_class = PostFilter
    paginate_by = 5
    ordering = ['-published_date']


class CategoryDetailView(DetailView):
    model = Category