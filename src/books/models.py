from django.db import models

# Create your models here.
from django.db import models

from django.conf import settings

from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db.models.signals import pre_save

from django.urls import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class Category(models.Model):
	title = models.CharField(max_length=120, blank=False, null=False)
	slug = models.SlugField(blank=True, null=True, editable=False)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('books:category_detail', kwargs = {'slug': self.slug})

class Book(models.Model):
	category 	= models.ManyToManyField(Category, related_name='books')
	title 		= models.CharField(max_length=120, blank=False, null=False)
	active		= models.BooleanField(default=False)
	description = models.TextField(max_length=500, blank=True, null=True)
	slug 		= models.SlugField(blank=True, null=True, editable=False)
	#image 		= models.ImageField(blank=True, null=True)
	url 		= models.URLField(max_length=200, blank=True, null=True)
	author 		= models.CharField(max_length=120, blank=True, null=True)
	timestamp 	= models.DateField(auto_now_add=True, editable=False)
	updated 	= models.DateField(auto_now=True, editable=False)
	date 		= models.DateField(blank=True, null=True)

	ratings		= []
	average 	= models.FloatField(default=5)

	class Meta:
		ordering = ['-average']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('books:book_detail', kwargs = {'slug': self.slug})

	def rate(self, vote):
		self.ratings.append(float(vote))
		self.average = sum(self.ratings)/float(len(self.ratings))

class Chapter(models.Model):
	book 	= models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False)
	title 	= models.CharField(max_length=120, blank=False, null=False)
	slug 	= models.SlugField(blank=True, null=True, editable=False)

	def __str__(self):
		return self.title

class Nugget(models.Model):
	user 		  = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
	book 		  = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False)
	chapter 	  = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)

	title 		  = models.CharField(max_length=160, blank=False, null=False)
	description	  = models.TextField(max_length=350, blank=True, null=True)
	active		  = models.BooleanField(default=False)
	rating		  = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)
	slug 		  = models.SlugField(blank=True, null=True, editable=False)
	timestamp 	  = models.DateField(auto_now_add=True, blank=True, null=True, editable=False)

	ratings		= []
	average 	= models.FloatField(default=5)

	class Meta:
		ordering = ['-average']

	def __str__(self):
		return self.title

	def rate(self, vote):
		self.ratings.append(float(vote))
		self.average = sum(self.ratings)/float(len(self.ratings))

class Review(models.Model):
	user 		= models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
	book 		= models.ForeignKey(Book, on_delete=models.CASCADE, blank=False, null=False)

	title		= models.CharField(max_length=160, blank=False, null=True)
	text 		= models.TextField(max_length=500, blank=False, null=False)
	rating 		= models.IntegerField(blank=False, null=False)
	timestamp 	= models.DateField(auto_now_add=True, null=True)

	def __str__(self):
		return self.book.title

	

def pre_save_category_receiver(sender, instance, *args, **kwargs):
	instance.slug = unique_slug_generator(instance)

def pre_save_book_receiver(sender, instance, *args, **kwargs):
	instance.slug = unique_slug_generator(instance)

def pre_save_chapter_receiver(sender, instance, *args, **kwargs):
	instance.slug = unique_slug_generator(instance)

def pre_save_nugget_receiver(sender, instance, *args, **kwargs):
	instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_category_receiver, sender=Category)
pre_save.connect(pre_save_book_receiver, sender = Book)
pre_save.connect(pre_save_chapter_receiver, sender = Chapter)
pre_save.connect(pre_save_nugget_receiver, sender = Nugget)




