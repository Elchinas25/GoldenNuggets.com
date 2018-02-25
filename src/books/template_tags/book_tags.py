from django import template

from django.db.models import Count

from books.models import Book, Category

register = template.Library()

@register.assignment_tag
def side_bar():
	return Category.objects.annotate(n_active_books=Count('books', filter=Q(book__active=True))).order_by('-n_active_books')