from django import forms
from django.contrib.auth.models import User


# class CommentForm(forms.ModelForm):
#     text = forms.Textarea


# class SendEmailForm(forms.Form):
#     subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
#     message = forms.CharField(widget=forms.Textarea)
#     users = forms.ModelMultipleChoiceField(label="To", queryset=User.objects.all(), widget=forms.SelectMultiple())
