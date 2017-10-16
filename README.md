# edc-sync-file-monitor

This module monitors files on a specified directory for a remote machine that  uses `edc-sync-files` module


### `Client`

A `Client` model is used to register remote machines whose files are monitored.

		class Client(ClientModelMixin, BaseUuidModel):

		    sftp_url = models.CharField(
		        verbose_name="SFTP Server url or IP Address",
		        max_length=250,
		        unique=True)
		
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
		        
The `paramiko` package is used to connect to remote machines and list files on a specified directory throw a model mixin `ClientModelMixin`.


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
		            ftp.close()
		        return files
		
		    @property
		    def ping_remote_client(self):
		        """Return True if remote machine is up.
		        """
		        return True if os.system("ping -c 1 " + self.sftp_url) is 0 else False
		
		    class Meta:
		        abstract = True

A report lie the diagram below will show a list of machine and the status for files and connectivity.

![Alt text](report.png?raw=true "Optional Title")


## A lot can still be improved on this module in terms of speed to return the starts and better approach to get the starts.

If the color is green for a panel there are no issue if yellow then there are pending files and red means no connection, lastly default grey color means site is disabled.

