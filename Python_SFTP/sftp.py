import paramiko
client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='localhost',username='maryam',password='123456',allow_agent=False,look_for_keys=False)
sftp=client.open_sftp()
sftp.put('test.txt','uploaded3.txt')
sftp.close()
