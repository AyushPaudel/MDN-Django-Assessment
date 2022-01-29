from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),

    path('blogger/<int:pk>', views.BloggerDetail.as_view(), name='blogs-by-author'),
    path('bloggers/', views.BloggerListView.as_view(), name='blogger-list'),

    path('myblogs/', views.BlogsByUser.as_view(), name='my-blogs'),

    path('blog/<int:pk>/comment/', views.BlogComment.as_view(), name='blog_comment')

]