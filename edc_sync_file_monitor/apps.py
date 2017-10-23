from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_sync_file_monitor'
    base_template_name = 'edc_base/base.html'
    project_name = 'EDC SYNC FILE MONITOR'
    institution = 'Botswana-Harvard AIDS Institute Partnership'

    protocol_sites = {
        'BCPP Communities': 'bhp066_community',
        'BCPP Central Server': 'bhp066_central_server',
        'BCPP Clinic Communities': 'bhp066_clinic_community',
        'BCPP Clinic Central Server': 'bhp066_clinic_central_server'}
