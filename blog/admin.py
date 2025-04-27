from django.conf import settings
from django.contrib import admin
from .models import Post, Category
# Register your models here.

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}


