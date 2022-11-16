from django.contrib import admin
from news_portal.models import Comment, Contact, News, Category, Newsletter, Tag

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Newsletter)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'message', 'post')

admin.site.register(Comment, CommentAdmin)