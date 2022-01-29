from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    post_date = models.DateField(default= date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])


class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField()

    class Meta:
        verbose_name_plural = 'Author'
        ordering=['user', 'bio']

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username



class Comments(models.Model):
    blog = models.ForeignKey('blog', on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        length = 40
        if len(self.comment) > length:
            return self.comment[:length] + "..."
        return self.comment
