from django.shortcuts import render

from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Chapter, Book, Category, Nugget, Review

class CategoryListView(ListView):
	template_name = 'books/categories.html'

	def get_queryset(self):
		return Category.objects.all()

class CategoryDetailView(DetailView):
	template_name = 'books/category_detail.html'

	def get_queryset(self):
		return Category.objects.all()
	
class BookDetailView(DetailView):
	def get_queryset(self):
		return Book.objects.all()

class BookReview(ListView):
	template_name = 'reviews.html'
	def get_queryset(self):
		return Review.objects.all() 