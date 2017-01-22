import paramiko

host = raw_input("Enter host: ")
user = raw_input("Enter user: ")
password = raw_input('Enter the password of ' +str(host) +' user ' +str(user) +': ')

def connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password)
    return ssh

def command(ssh):
    transport = ssh.get_transport()
    session = transport.open_session()
    session.set_combine_stderr(True)
    session.get_pty()

    #taking the command to be executed at run time
    comm = raw_input("\nInput the command to be executed: ")
    session.exec_command(comm)
    stdin = session.makefile('wb', -1)
    stdout = session.makefile('rb', -1)
    print stdout.read()

    #with open('SampleWrite.txt', 'w') as w:
        #w.write(stdout.read())
    # print (stdout.read())    why cant we call it again
    stdin.flush()

#write contents of the command from server to local machine and close the connection
if __name__ == '__main__':
    ssh = connection()
    feedback = 'y'
    while feedback.lower() == 'y':
        c = command(ssh)
        feedback = raw_input("Do you want other command to be executed (y/n): ")
    else:
        ssh.close()



