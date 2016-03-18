# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
    Admin View for Post
    '''
    list_display = ('title', 'author', 'written_in', 'last_edited')
    list_filter = ('author',)
    readonly_fields = ('content',)
    search_fields = ('title', 'author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Admin View for Comment
    '''
    list_display = ('title', 'written_in', 'last_edited')
    list_filter = ('post', 'commentator')
    readonly_fields = ('content',)
    search_fields = ('post', 'commentator', 'written_in')

    def title(self, obj):
        return str(obj)