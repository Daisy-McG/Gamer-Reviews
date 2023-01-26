from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form to create review """
    class Meta:
        model = Review
        fields = ['title', 'game_name', 'content', 'image', 'rating']

        content = forms.CharField(widget=RichTextWidget())

        labels = {
            'title': 'Review Title',
            'game_name': 'Game Name',
            'content': 'Review',
            'image': 'Game Image',
            'rating': 'Rating'
        }
