# -*- coding: utf-8 -*-
from django import forms
from rawauth.models import Author


class AuthorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return password2

    def save(self, commit=True):
        author = super(AuthorRegistrationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        author.set_password(password)
        if commit:
            author.save()
        return author
