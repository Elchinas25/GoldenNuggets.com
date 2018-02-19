from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.i18n import i18n_patterns

from .views import CategoryListView, CategoryDetailView, BookDetailView, BookReview

urlpatterns = [
	url(r'^categories/$', CategoryListView.as_view(), name='categories'),
	url(r'^categories/(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='category_detail'),
	url(r'^(?P<slug>[\w-]+)/$', BookDetailView.as_view(), name='book_detail'),
	url(r'^(?P<slug>[\w-]+)/reviews/$', BookReview.as_view(), name='reviews'),
]