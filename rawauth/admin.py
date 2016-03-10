from django.contrib import admin
from rawauth.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    '''
        Admin View for Author
    '''
    list_display = ('full_name', 'email')
    list_filter = ('first_name', 'last_name',)
    readonly_fields = ('username',)
    search_fields = ('username', 'last_name', 'first_name', 'email')

    def full_name(self, obj):
        return obj.get_full_name()