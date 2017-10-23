from edc_base.model_mixins import BaseUuidModel
from django.db import models

from .client_model_mixin import ClientModelMixin


class Client(ClientModelMixin, BaseUuidModel):

    sftp_url = models.CharField(
        verbose_name="SFTP Server url or IP Address",
        max_length=250)

    sftp_user = models.CharField(
        verbose_name="SFTP Username",
        max_length=100)

    sftp_pass = models.CharField(
        verbose_name="SFTP Password",
        max_length=100)

    active = models.BooleanField(
        default=False,
        verbose_name="Client active status",)

    has_files = models.BooleanField(
        default=False)

    ping = models.BooleanField(
        default=False)

    remote_dirname = models.CharField(
        verbose_name="Client monitored directory",
        max_length=250,
        null=True)

    protocol = models.CharField(
        verbose_name="Protocol Name",
        max_length=250,
        null=True)

    def __str__(self):
        return f'{self.sftp_url} {self.protocol}'

    class Meta:
        app_label = 'edc_sync_file_monitor'
        unique_together = (
            ('sftp_url', 'remote_dirname'))
