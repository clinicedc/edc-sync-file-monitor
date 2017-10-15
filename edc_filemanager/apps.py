from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_filemanager'
    base_template_name = 'edc_base/base.html'
