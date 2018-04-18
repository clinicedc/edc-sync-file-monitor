from django.apps import apps as django_apps
from django.views.generic.base import ContextMixin

from ..models import Client


class SiteMonitoringStartViewMixin(ContextMixin):

    app_config = django_apps.get_app_config('edc_sync_file_monitor')
    client_model_cls = Client

    def is_divisible_by_3(self, number):
        if number % 3 == 0:
            return True
        return False

    def report_data(self, protocol=None):
        report_data = {}
        clients = self.client_model_cls.objects.filter(protocol=protocol)
        clients_list = []
        for index, client in enumerate(clients):
            if client.active:
                client.ping = True if client.ping_remote_client else False
                client.save()
                client.has_files = True if client.remote_files else False
            else:
                client.has_files = False
            client.save()
            clients_list.append(client)
            if clients.count() < 3:
                report_data['less_3'] = clients
                return report_data
            elif self.is_divisible_by_3(index + 1):
                report_data[index + 1] = clients_list
                clients_list = []
            elif not self.is_divisible_by_3(clients.count()) and clients.count() > 3:
                if clients.count() == index + 1:
                    report_data[index + 1] = clients_list
        return report_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_value = self.kwargs.get('site_value', None)
        site_key = list(self.app_config.protocol_sites.keys())[
            list(self.app_config.protocol_sites.values()).index(site_value)]
        context.update(
            report_data=self.report_data(protocol=site_value),
            site=site_key)
        return context
