from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BlogByAuthorView.as_view(), name='blog-by-author'),
    path('myblogs/', views.BlogsByUser.as_view(), name='my-blogs'),

    path('blogger/<int:pk>', views.BlogByAuthorView.as_view(), name='blog-by-author'),
    path('bloggers/', views.BloggerListView.as_view(), name='blogger-lisst'),
    path('blog/<int:pk>/comment/', views.BlogComment.as_view, name='blog_comment')

]