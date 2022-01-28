from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Blogger, Comments

def index(request):
    return render(request, 'index.html')

class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class BlogsByUser(LoginRequiredMixin, generic.ListView):
    model = Blog
    template_name = 'catalog/blogs_by_user.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.filter(borrower=self.request.user).order_by('-post_date')

class BloggerListView(generic.ListView):
    model = Blogger
    template_name = 'blogger_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Blogger.objects.all()


class BlogByAuthorView(generic.ListView):
    pass





class BlogComment(LoginRequiredMixin, CreateView):
    pass

