# -*- coding: utf-8 -*-
from blog.models import Post
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rawauth.models import Author
from rawauth.mixins import RawLoginRequiredMixin


class PostCreateView(RawLoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blog:posts')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(pk=self.request.user.pk)
        post.slug = slugify(post.title)
        post.save()
        return HttpResponseRedirect(self.get_success_url())
post_create_view = PostCreateView.as_view()


class PostListView(ListView):
    model = Post
post_list_view = PostListView.as_view()


class PostDetailView(DetailView):
    model = Post
post_view = PostDetailView.as_view()


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
post_update_view = PostUpdateView.as_view()
        