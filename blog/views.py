from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Blogger, Comments


def index(request):
    return render(request, 'index.html')


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'



class BloggerListView(generic.ListView):
    model = Blogger
    template_name = 'blog/blogger_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Blogger.objects.all()


class BloggerDetail(generic.DetailView):
    model = Blogger
    template_name = 'blog/blogger_detail.html'



class BlogsByUser(LoginRequiredMixin, generic.ListView):
    model = Blogger
    template_name = 'blog/blogs_by_user.html'
    paginate_by = 5

    def get_queryset(self):
        return Blogger.objects.filter(user=self.request.user)


class BlogComment(LoginRequiredMixin, CreateView):

    """
    Form for adding a blog comment. Requires login.
    """
    model = Comments
    fields = ['comment',]



    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(BlogComment, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context


    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(BlogComment, self).form_valid(form)


    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })
