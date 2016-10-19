import paramiko

l_host = raw_input("Enter host: ")
l_user = raw_input("Enter user: ")
l_password = raw_input('Enter the password of ' +str(l_host) +' user ' +str(l_user) +': ')

def connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(l_host, username=l_user, password=l_password)
    return ssh

def command(ssh):
    transport = ssh.get_transport()
    session = transport.open_session()
    session.set_combine_stderr(True)
    session.get_pty()
    session.exec_command("ls -l")
    stdin = session.makefile('wb', -1)
    stdout = session.makefile('rb', -1)

    with open('SampleWrite.txt', 'w') as w:
        w.write(stdout.read())
    # print (stdout.read())    why cant we call it again
    stdin.flush()

#write contents of the command from server to local machine and close the connection
if __name__ == '__main__':
    ssh = connection()
    c = command(ssh)
    ssh.close()



