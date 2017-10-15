from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'EDC Filemanager'
    site_header = 'EDC Filemanager'
    index_title = 'EDC Filemanager'
    site_url = '/edc_filemanager/list/'


edc_filemanager_admin = AdminSite(name='edc_filemanager_admin')
