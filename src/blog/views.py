from django.views.generic import ListView, DetailView
from .models import Post


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
