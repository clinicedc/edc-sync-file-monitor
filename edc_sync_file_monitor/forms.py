from django import forms

from edc_base.modelform_mixins import JSONModelFormMixin, CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin
from .models import Client


class ClientForm(FormValidatorMixin, CommonCleanModelFormMixin,
                 JSONModelFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'sftp_pass': forms.PasswordInput(),
        }
