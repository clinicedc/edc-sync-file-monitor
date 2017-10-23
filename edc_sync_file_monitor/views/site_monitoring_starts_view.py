from django.apps import apps as django_apps

from ..models import Client


class SiteMonitoringStartView:

    app_config = django_apps.get_app_config('edc_sync_file_monitor')

    def clients(self, site_value=None):
        return Client.objects.filter(protocol=site_value)

    def is_divisible_by_3(self, number):
        if number % 3 == 0:
            return True
        return False

    def report_data(self, site_value=None):
        report_data = {}
        clients = self.clients(site_value=site_value)
        total_clients = clients.count()
        count = 1
        clients_list = []
        for client in clients:
            if client.active:
                client.ping = True if client.ping_remote_client else False
                client.save()
                client.has_files = True if client.remote_files else False
            else:
                client.has_files = False
            client.save()
            clients_list.append(client)
            if total_clients < 3:
                report_data['less_3'] = clients
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
        site_value = self.kwargs.get('site_value', None)
        site_key = list(self.app_config.protocol_sites.keys())[
            list(self.app_config.protocol_sites.values()).index(site_value)]
        context.update(
            report_data=self.report_data(site_value=site_value),
            site=site_key)
        return context
