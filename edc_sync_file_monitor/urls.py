from django.urls import path, re_path

from .admin_site import edc_sync_file_monitor_admin
from .views import ReportView, HomeView


app_name = 'edc_sync_file_monitor'

urlpatterns = [
    path(r'admin/', edc_sync_file_monitor_admin.urls),
    re_path(r'^file_monitor_report/(?P<site_value>\w+)/$',
            ReportView.as_view(), name='file_monitor_report_url'),
    path(r'', HomeView.as_view(), name='home_url'),
]
