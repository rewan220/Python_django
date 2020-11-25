from django.contrib import admin
from snippet_test.models import SnippetTest


# Register your models here.

class SnippetAdmin(admin.ModelAdmin):
	list_display = ('id','title','subject','url', 'date_published', 'date_updated','author')
	search_fields = ('title','subject',)
	readonly_fields=('date_published', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(SnippetTest, SnippetAdmin)
