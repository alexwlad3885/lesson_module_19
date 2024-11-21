from django.contrib import admin
from .models import Category, News, Author, PublicationSite


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PublicationSite)
admin.site.register(News)
