#Import paramiko library
import paramiko

#Define a function called ssh_commang that takes 5 args
def ssh_command(ip, port, user, passwd, cmd):
    #Create an instance of the SSH Client class from paramiko
    client = paramiko.SSHClient()
    #If the SSH servers host key is not found in the local host key database, the servers hostkey will be automatically added
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #Establish SSH connection to the server using provided IP, Username and Password
    client.connect(ip, port=port, username=user, password=passwd)

    #Execute the command on the server and recieve items in response
    _, stdout, stderr = client.exec_command(cmd)
    #Read the lines from stout and stderr and combine them into an output to print
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Output---')
        for line in output:
            print(line.strip())


#Import getpass and handle user inputs, set default values if necessary
if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)