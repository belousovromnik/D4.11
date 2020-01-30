from django import forms  
from p_library.models import Author, Book, Bookreader
from reader.models import Reader
  
class AuthorForm(forms.ModelForm):  

    full_name = forms.CharField(label='Автор',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите автора'}))
    birth_year = forms.IntegerField(label='Год рождения',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите год рождения'}))
    country = forms.CharField(label='Страна',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите страну'}))
    
    class Meta:  
        model = Author  
        fields = '__all__'


class BookreaderForm(forms.ModelForm):
    book = forms.ModelChoiceField(label='Книга', queryset=Book.objects.all(),
                                       widget=forms.Select(
                                           attrs={'class': 'form-control',
                                                  'placeholder': 'Книга'}))
    reader = forms.ModelChoiceField(label='Читатель', queryset=Reader.objects.all(),
                                     widget=forms.Select(
                                         attrs={'class': 'form-control',
                                                'placeholder': 'Читатель'}))
    comment = forms.CharField(label='Комментарий',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Комментарий'}))

    class Meta(object):
        model = Bookreader
        fields = ('book', 'reader', 'comment')
