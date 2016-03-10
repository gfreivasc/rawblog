# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
        Admin View for Post
    '''
    list_display = ('title', 'author', 'written_in', 'last_edited')
    list_filter = ('author',)
    readonly_fields = ('content',)
    search_fields = ('title', 'author',)