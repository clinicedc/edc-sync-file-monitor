from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin

from .site_monitoring_starts_view import SiteMonitoringStartView


class ReportView(SiteMonitoringStartView, EdcBaseViewMixin, TemplateView):

    app_config_name = 'edc_sync_file_monitor'
    template_name = 'edc_sync_file_monitor/report.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config('edc_sync_file_monitor')
        context.update(
            project_name=app_config.project_name,
            institution=app_config.institution)
        return context
