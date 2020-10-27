rom django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"First Name"}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Last Name"}))
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Username"}))
    email = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control",
                                                                "placeholder":"Email"}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                "placeholder":"Password"}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class":"form-control",
                                                                "placeholder":"Confirm Password"}))
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"