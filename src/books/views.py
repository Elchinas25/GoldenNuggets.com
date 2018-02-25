from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.http import HttpResponse

from django.db.models import Count
from django.db.models import Q

from .models import Chapter, Book, Category, Nugget, Review
from .forms import ReviewForm

class CategoryListView(ListView):
	template_name = 'books/categories.html'

	def get_queryset(self):
		return Category.objects.all()


class CategoryDetailView(DetailView):
	template_name = 'books/category_detail.html'

	def get_queryset(self):
		return Category.objects.all().annotate(n_books = Count('books'))
	


class BookDetailView(DetailView):
	def get_queryset(self):
		return Book.objects.annotate(n_reviews=Count('review'))

	def post(self, *args, **kwargs):
		self.object = self.get_object(self.get_queryset()) 
		print('Before', self.object.ratings)
		rating = int(self.request.POST.get('rating_form'))
		self.object.rate(vote=rating)
		self.object.save()
		print('After', self.object.ratings)
		ctx = self.get_context_data(**kwargs)
		ctx['message'] = 'Your rating has been saved, thanks!'

		return render(self.request, 'books/book_detail.html', ctx)


class Reviews(DetailView):
	template_name = 'books/reviews.html'
	def get_queryset(self):
		return Book.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if get_language() == 'es':
			context['reviews'] = self.object.review_set.all().filter(Q(language='es') | Q(language='all'))
		else:
			context['reviews'] = self.object.review_set.all().filter(Q(language='en') | Q(language='all'))

		context['form'] = ReviewForm()

		return context

	def post(self, *args, **kwargs):
		self.object = self.get_object(self.get_queryset())
		form = ReviewForm(self.request.POST)
		context = self.get_context_data(**kwargs)

		if form.is_valid():
			obj = form.save(commit=False)
			obj.book = self.object
			obj.user = self.request.user
			obj.language = get_language()
			obj.save()
			context['message'] = 'Your review has been successfully saved! Thanks for your help to the community.'

			return render(self.request, 'books/reviews.html', context)

		else:
			context.update({'form': form})
			return render(self.request, 'books/reviews.html', context)

	






	

# class CreateReview(CreateView):
# 	template_name = 'books/create_review.html'
# 	form_class = ReviewForm

# 	def form_valid(self, form):
# 		obj = form.save(commit=False)
# 		return super().form_valid(form)

# class BookLoc(CreateView):
# 	template_name = 'books/book_detail.html'
# 	form_class = ReviewForm
# 	success_url = '/books/categories/'

# 	def get_context_data(self, *args, **kwargs):
# 		context = super().get_context_data(*args, **kwargs)

# 		slug = self.kwargs.get('slug')
# 		obj = Book.objects.get(slug__iexact=slug)

# 		if get_language() == 'es':
# 			context['reviews'] = obj.review_set.all().filter(language__iexact='es')
# 		else:
# 			context['reviews'] = obj.review_set.all().filter(language__iexact='en')

# 		if len(context['reviews']) == 0:
# 			context['is_empty'] = True

# 		context['object'] = obj
# 		return context

# 	def form_valid(self, form):
# 		obj = form.save(commit=False)

# 		return super().form_valid(form)

# 	def get_form_kwargs(self, *args, **kwargs):
# 		kwargs = super().get_form_kwargs(*args, **kwargs)
# 		kwargs['user'] = self.request.user
# 		# kwargs['book'] = 
# 		kwargs['language'] = get_language()

# 		return kwargs
