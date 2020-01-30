from django import forms  
from .models import Reader
  
class ReaderForm(forms.ModelForm):  

    full_name = forms.CharField(label='ФИО',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите ФИО читателя'}))
    birth_year = forms.IntegerField(label='Год рождения',
                           widget=forms.NumberInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите год рождения'}))
    comment = forms.CharField(label='Комментарий',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите комментарий'}))
    
    class Meta:  
        model = Reader  
        fields = '__all__'
