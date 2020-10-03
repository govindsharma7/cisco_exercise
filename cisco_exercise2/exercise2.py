from paramiko import SSHClient, AutoAddPolicy

''' EXERCISE 2, point no. 1 '''
# to telnet to a server
# telnet <ip address> <port no>

ssh = SSHClient()
ssh.load_system_host_keys()  # to look for trusted hosts
# to add the host if not already added
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect('49.36.141.4', username='govind', password='123456789')

# to check disk usage
print("//////////////Disk Usage//////////////")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('df -H')
for i in ssh_stdout:
    print(i.strip('\n'))

# to check inode usage
print("//////////////iNode Usage//////////////")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('df -i')
for i in ssh_stdout:
    print(i.strip('\n'))

# to list files & directory
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cd code/; ls -l')
for i in ssh_stdout:
    print(i.strip('\n'))

# to use ftp & sftp
# ftp <ip address>
# <username>
# <password>
# cp <source> <destination>
#
# sftp <username>@<ip address>
# <password>
# cp <source> <destination>

# to scp a file to remote server
# scp filename.txt <username>@<ip address>:/directory
# when we hit enter it will ask for password for the username provided to
# connect remote server


''' EXERCISE 2, point no. 2 '''
# telnet <ip address> <port no>
# sftp <username>@<ip address>
# <password>
# to create file we can use `touch <filename>` command
# to create zip we can use `zip remote_dir.zip remote_dir/` command
# tftp -l <FileName> -p <TFTP Server IP> <Port No of TFTP>
# to unzip file we can use `unzip remote_dir.zip` command


''' EXERCISE 2, point no. 3 '''
# Let say the threshold value of number of processes for apache is 1000.
# So, if the processes go near 1000 then we need to restart apache
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
    'ps aux | grep httpd | wc -l')  # to check number of httpd processes
for i in ssh_stdout:
    httpd_processes_count = i.strip('\n')

if httpd_processes_count >= 990:
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(
        '/etc/init.d/httpd restart')  # to restart apache service
