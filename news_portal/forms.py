from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news_portal.models import News, Contact, Newsletter, Comment

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({"class":"form-control","placeholder":"Enter your username"})
        self.fields['first_name'].widget.attrs.update({"class":"form-control","placeholder":"Enter your first name"})
        self.fields['last_name'].widget.attrs.update({"class":"form-control","placeholder":"Enter your last name"})
        self.fields['email'].widget.attrs.update({"class":"form-control","placeholder":"Enter your email"})
        self.fields['password1'].widget.attrs.update({"class":"form-control","placeholder":"Enter your password"})
        self.fields['password2'].widget.attrs.update({"class":"form-control","placeholder":"Confirm your password"})

    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ("title", "category", "tag", "image", "content")
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "required":True}),
            "category": forms.Select(attrs={"class":"form-control", "required":True}),
            "tag": forms.SelectMultiple(attrs={"class":"form-control", "required":True}),
            "content": forms.Textarea(attrs={"class":"form-control", "required":True})
        } 

class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class Newsletter(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
        
class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields= "__all__"