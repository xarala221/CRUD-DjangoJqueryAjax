from django import forms
from .models import Book, Seller
#from simple_autocomplete.widgets import AutoCompleteWidget
"""class BookForm(forms.ModelForm):
  	seller = forms.ModelChoiceField(queryset=Seller.objects.all())
    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type','seller' )
"""

class BookForm(forms.ModelForm):
  #seller = forms.ModelChoiceField(queryset=Seller.objects.all(), initial=3, widget=AutoCompleteWidget(url='/custom-json-jquery', initial_display='amazon'))
  #seller = forms.ModelChoiceField(label='Seller', queryset=Seller.objects.all(),widget=AutoCompleteWidget)
  #weight = forms.CharField(max_length=254,label='Largeur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
  #length = forms.CharField(max_length=254,label='Longueur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
  #height = forms.CharField(max_length=254,label='Hauteur',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
  #width = forms.CharField(max_length=254,label='Poids',widget=forms.TextInput({'class': 'form-control','placeholder': ''}))
  class Meta:
    model = Book
    fields = [
      'title', 'publication_date', 'author', 'price', 'pages', 'book_type','seller' 
    ]
