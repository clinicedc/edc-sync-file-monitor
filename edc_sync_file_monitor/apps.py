from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_sync_file_monitor'
    base_template_name = 'edc_base/base.html'
    project_name = 'EDC SYNC FILE MONITOR'
    institution = 'Botswana-Harvard AIDS Institute Partnership'
