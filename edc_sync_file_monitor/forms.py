from django import forms

from edc_base.modelform_mixins import JSONModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin
from .models import Client


class ClientForm(FormValidatorMixin, JSONModelFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'sftp_pass': forms.PasswordInput(),
        }
