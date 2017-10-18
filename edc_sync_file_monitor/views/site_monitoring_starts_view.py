from ..models import Client


class SiteMonitoringStartView:

    @property
    def clients(self):
        return Client.objects.all()

    def is_divisible_by_3(self, number):
        if number % 3 == 0:
            return True
        return False

    @property
    def report_data(self):
        report_data = {}
        total_clients = self.clients.count()
        count = 1
        clients_list = []
        for client in self.clients:
            if client.active:
                client.ping = True if client.ping_remote_client else False
                client.save()
                client.has_files = True if client.remote_files else False
            else:
                client.has_files = False
            client.save()
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
        context.update(
            report_data=self.report_data,)
        return context
