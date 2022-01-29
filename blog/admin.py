from django.contrib import admin
from .models import Blog, Blogger, Comments

admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Comments)