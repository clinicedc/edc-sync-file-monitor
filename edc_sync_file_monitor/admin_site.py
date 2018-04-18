from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Data Synchronization File Monitor'
    site_header = 'Data Synchronization File Monitor'
    index_title = 'Data Synchronization File Monitor'
    site_url = '/edc_sync_file_monitor/list/'


edc_sync_file_monitor_admin = AdminSite(name='edc_sync_file_monitor_admin')
