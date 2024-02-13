from django import forms

class SignUpForm(forms.Form):
    # username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"username"}))
    phone = forms.IntegerField(max_value=9999999999, min_value=0, widget=forms.NumberInput(attrs={"class":"phone"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"pass":"pass"}))

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"pass": "pass"}))
