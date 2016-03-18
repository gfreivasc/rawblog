# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from blog.models import Comment


class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    email = forms.EmailField(required=True)

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['content'].required = True
