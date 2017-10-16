from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin

from ..models import Client


class HomeView(EdcBaseViewMixin, TemplateView):

    app_config_name = 'edc_sync_file_monitor'
    template_name = 'edc_sync_file_monitor/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @property
    def clients(self):
        return Client.objects.all()

    def is_divisible_by_3(self, number):
        if number % 3 == 0:
            return True
        return False

    def update_file_status(self):
        for client in self.clients:
            if client.active:
                client.has_files = True if client.remote_files else False
            else:
                client.has_files = False
            client.save()

    @property
    def report_data(self):
        report_data = {}
        total_clients = self.clients.count()
        count = 1
        clients_list = []
        for client in self.clients:
            clients_list.append(client)
            if total_clients < 3:
                report_data['less_3'] = self.clients
                return report_data
            elif self.is_divisible_by_3(count):
                report_data[count] = clients_list
                clients_list = []
            elif not self.is_divisible_by_3(total_clients) and total_clients > 3:
                if total_clients == count:
                    report_data[count] = clients_list
            count += 1
        return report_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config('edc_sync_file_monitor')
        self.update_file_status()
        context.update(
            report_data=self.report_data,
            project_name=app_config.project_name,
            institution=app_config.institution)
        return context
