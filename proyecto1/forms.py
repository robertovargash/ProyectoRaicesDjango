from pyexpat import model
from django.forms import *
from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.models import User,Permission, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UsernameField

class AddUserForm(UserCreationForm):
    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','is_staff','is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class PermissionsModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return (obj.codename)

class EditUserForm(forms.ModelForm):
    email = forms.EmailField(label=_('Email'),
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':_('Email')}),
    )
    username = forms.CharField(label=_('Username'),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Username')}),
    )
    first_name = forms.CharField(label=_('First_Name'),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('First_Name')}),
    )
    last_name = forms.CharField(label=_('Last_Name'),
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Last_Name')}),
    )
    user_permissions = PermissionsModelMultipleChoiceField(label=_('User_permissions'),queryset=Permission.objects.all(),widget=SelectMultiple(attrs={'data-dropdown-css-class':'select2-red','style':'width: 100%;','class':'select2 select2-purple form-control multiple','data-placeholder':_('Select_a_Permission_Select_multiple')}))
    groups = forms.ModelMultipleChoiceField(label=_('User_groups'),queryset=Group.objects.all(),widget=SelectMultiple(attrs={'data-dropdown-css-class':'select2-red','style':'width: 100%;','class':'select2 select2-purple form-control multiple','data-placeholder':_('Select_a_Group_Select_multiple')}))
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","user_permissions","groups")
        field_classes = {"username": UsernameField}