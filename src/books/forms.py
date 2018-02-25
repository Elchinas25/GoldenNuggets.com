from .models import Review

from modeltranslation.forms import TranslationModelForm

class ReviewForm(TranslationModelForm):
	class Meta:
		model = Review
		fields = ['title', 'text', 'rating']

	# def __init__(self, user, language, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	print(user)
	# 	self.user = user
	# 	# self.book = book
	# 	self.language = language

		
