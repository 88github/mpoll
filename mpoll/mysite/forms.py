#coding=utf-8
from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='小白')
    user_email = forms.EmailField(label='电子邮件')
    user_message = forms.CharField(label='您的意见', widget=forms.Textarea)