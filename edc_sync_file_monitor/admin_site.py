from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'EDC Filemanager'
    site_header = 'EDC Filemanager'
    index_title = 'EDC Filemanager'
    site_url = '/edc_sync_file_monitor/list/'


edc_sync_file_monitor_admin = AdminSite(name='edc_sync_file_monitor_admin')
