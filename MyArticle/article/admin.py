from django.contrib import admin

from .models import Articles, Extras

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('article_name', 'article_value', 'image_name')
	search_fields = ['article_name']

class ExtrasAdmin(admin.ModelAdmin):
	search_fields = ['rel_article_name']
	list_display = ('rel_article_name', 'image_name')
	
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Extras, ExtrasAdmin)
