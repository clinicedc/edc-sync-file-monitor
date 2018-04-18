from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin

from .site_monitoring_starts_view_mixin import SiteMonitoringStartViewMixin


class ReportView(EdcBaseViewMixin, SiteMonitoringStartViewMixin, TemplateView):

    app_config_name = 'edc_sync_file_monitor'
    template_name = 'edc_sync_file_monitor/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            project_name=self.app_config.project_name,
            institution=self.app_config.institution)
        return context
