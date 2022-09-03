from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { f:"" for f in fields }
        
class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Titulo Post'}), required=True)
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'Description Post'}), required=True)
    image = forms.ImageField(label='Select file', widget=forms.FileInput(attrs={'style': 'border:none;'}))
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']