from django.contrib import admin

from .models import Article, Comment
# Register your models here.

#Comment yorumlar için ekledik
admin.site.register(Comment)

#admin.site.register(Article)#kayıt etmek gerekiyor
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article
    list_display = ["title","author","created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]