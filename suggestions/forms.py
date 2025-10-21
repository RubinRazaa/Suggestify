from django import forms
from .models import Suggestion,Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'description']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control rounded-3 shadow-sm', 'rows':4, 'placeholder':'Write a comment...', 'style':'resize:none'})
        }