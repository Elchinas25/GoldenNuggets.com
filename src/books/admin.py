from django.contrib import admin

from .models import Book, Chapter, Nugget, Category

# class NuggetInline(admin.TabularInline):
# 	model = Nugget
# 	# fields = ['title']
# 	# fields = ['user', 'book', 'chapter', 'golden_nugget', 'description', 'rating', 'active', 'slug']
# 	# fieldsets = (
# 	# 		(Associations: {

# 	# 			}),
# 	# 	)

class NuggetInline(admin.TabularInline):
    model = Nugget


class ChapterAdmin(admin.StackedInline):
	model = Chapter
	inlines = [
        NuggetInline,
    ]

class BookAdmin(admin.ModelAdmin):
	list_filter = ('category',)
	inlines = [
        ChapterAdmin,
        NuggetInline,
    ]
	

admin.site.register(Category)
admin.site.register(Book, BookAdmin)
# admin.site.register(Chapter, ChapterAdmin)


