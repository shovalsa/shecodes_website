from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    join_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'join_date', 'password1', 'password2', )

class MyForm(forms.Form):
  def as_contact(self):
    return self._html_output(
        normal_row='<p%(html_class_attr)s> %(label)s <br> %(field)s %(help_text)s </p>',
        error_row='%s',
        row_ender='</p>',
        help_text_html=' <span class="helptext">%s</span>',
        errors_on_separate_row=True)

class ContactForm(MyForm):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
