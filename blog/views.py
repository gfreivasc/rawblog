# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rawauth.models import Author
from rawauth.mixins import RawLoginRequiredMixin
from blog.models import Post


class PostCreateView(RawLoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blog:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(pk=self.request.user.pk)
        post.save()
        return HttpResponseRedirect(self.get_success_url())
post_create_view = PostCreateView.as_view()


class PostListView(ListView):
    model = Post
post_list_view = PostListView.as_view()
