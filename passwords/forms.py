from django import forms
from passwords.models import StoredPassword

class AddPasswordForm(forms.ModelForm):
    class Meta:
        model = StoredPassword
        fields = ['url', 'username', 'encrypted_password']
        labels = {
            'url': 'URL',
            'encrypted_password': 'Password',
        }