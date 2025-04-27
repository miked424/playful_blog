from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Yoour Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, label="Your message")
