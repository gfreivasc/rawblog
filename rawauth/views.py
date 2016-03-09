# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from rawauth.forms import AuthorRegistrationForm


class AuthorCreateView(CreateView):
    """Class that handles author creation"""
    form_class = AuthorRegistrationForm
    template_name = 'rawauth/registration.html'
    success_url = reverse_lazy('blog:posts')

    def form_valid(self, form):
        valid = super(AuthorCreateView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    # def get_context_data(self, **kwargs):
    #     context = super(AuthorCreateView, self).get_context_data(**kwargs)
    #     context['next'] = self.request.GET['next']
    #     return context

    def get_success_url(self):
        return self.request.GET.get(
            'next',
            super(AuthorCreateView, self).get_success_url())
author_create_view = AuthorCreateView.as_view()
