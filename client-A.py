import socket

host = "localhost"
port = 12345
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    num = str(s.recv(1024).decode('ascii'))
    if num == 'Server is Busy!\n':
        print(num)
        break
    else:
        print(num)
    message = input("Enter First Num:\n")
    s.sendall(message.encode('ascii'))
    message = input("Enter Second Num:\n")
    s.sendall(message.encode('ascii'))
    num = str(s.recv(1024).decode('ascii'))
    print('Answer is: ', num, '\n')
    num = input('Do you want to continue(y/n): ')
    if num == 'y':
        continue
    else:
        s.sendall(b'DONE')
        break

s.close()
