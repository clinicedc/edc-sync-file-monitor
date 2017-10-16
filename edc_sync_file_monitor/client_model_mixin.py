import os
import paramiko

from django.db import models


class ClientModelMixin(models.Model):

    @property
    def remote_files(self):
        """Returns a list of remote files for a given directory.
        """
        files = []
        if self.ping_remote_client:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(
                self.sftp_url, username=self.sftp_user, password=self.sftp_pass)
            ftp = ssh.open_sftp()
            if self.remote_dirname:
                ftp.chdir(self.remote_dirname)
            files = ftp.listdir()
            files = [file for file in files if file.endswith('.json')]
            ftp.close()
        return files

    @property
    def ping_remote_client(self):
        """Return True if remote machine is up.
        """
        return True if os.system("ping -c 1 " + self.sftp_url) is 0 else False

    class Meta:
        abstract = True
