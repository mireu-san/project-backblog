from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'is_approved')  # Renamed 'active' to 'is_approved'
    list_filter = ('is_approved', 'created_on')  # Renamed 'active' to 'is_approved'
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)  # Renamed 'active' to 'is_approved'
