from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text=_('Optional'), label=_('First name'))
    last_name = forms.CharField(max_length=30, required=False, help_text=_('Optional'), label=_('Last name'))
    email = forms.EmailField(max_length=254, help_text=_('Required. Inform a valid email address.'), label=_('Email address'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('track', 'main_branch', 'personal_background')


class MyForm(forms.Form):
  def as_contact(self):
    return self._html_output(
        normal_row='<p%(html_class_attr)s> %(label)s <br> %(field)s %(help_text)s </p>',
        error_row='%s',
        row_ender='</p>',
        help_text_html=' <span class="helptext">%s</span>',
        errors_on_separate_row=True)

class ContactForm(MyForm):
    contact_name = forms.CharField(required=True, label=_("Name"))
    contact_email = forms.EmailField(required=True, label=_("Email"))
    subject = forms.CharField(required=True, label=_('Subject'))
    message = forms.CharField(required=True, widget=forms.Textarea, label=_('Message'))
