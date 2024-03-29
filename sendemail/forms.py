from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class': "input-color"}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': "input-color"}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "input-color"}), required=True)
    