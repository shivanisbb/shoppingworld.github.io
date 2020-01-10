from django import forms
from shop.models import contact,registration,login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class personad(forms.ModelForm):
        class Meta:
            model = contact
            fields = '__all__'
        message = forms.CharField(max_length=20, widget=forms.Textarea)


class regad (forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
    password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100 , widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password:')
        password2 = self.cleaned_data.get('confirm_password:')

        if password1 != password2:

            raise ValidationError("Password don't match")

        return password2
    def save(self, commit=True):
        user= user .objects.create_user(self.cleaned_data['email'],self.cleaned_data['password1'])
        return user

class loginad(forms.ModelForm):
            class Meta:
                model = login
                fields = '__all__'

            password = forms.CharField(max_length=100, widget=forms.PasswordInput)
