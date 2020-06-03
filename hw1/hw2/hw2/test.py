import paramiko
import sys
import multiprocessing

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


try:
    ssh.connect(SSH_ADDRESS + str(100), username=SSH_USERNAME, password=SSH_PASSWORD, timeout=5)
    with open(filename, "a") as f:
    	f.write(SSH_ADDRESS)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('passwd')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('maker')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('test')
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('test')
except Exception as e:
    sys.stderr.write("SSH connection error: {0}".format(e))

if ssh_stdout:
    sys.stdout.write(ssh_stdout.read())
if ssh_stderr:
    sys.stderr.write(ssh_stderr.read())