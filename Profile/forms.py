from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=128, label='Enter Email', required=True)
    password_first = forms.CharField(max_length=128, label='Enter Password', required=True, widget=forms.PasswordInput)
    password_second = forms.CharField(max_length=128, label='Re-Enter Password', required=True,
                                      widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=128, label='Enter Email', required=True)
    password = forms.CharField(max_length=128, label='Enter Password', required=True, widget=forms.PasswordInput)
