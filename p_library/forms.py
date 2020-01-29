from django import forms  
from p_library.models import Author  
  
class AuthorForm(forms.ModelForm):  

    full_name = forms.CharField(label='Автор',
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Введите автора'}))
    class Meta:  
        model = Author  
        fields = '__all__'
