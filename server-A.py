import socket, threading

def sumFunc(c, addr):
    global n
    print('Client at', addr[0], ':', addr[1], 'Connected!')
    n = n + 1
    print('Number of Connected Clients:', n)
    while True:
        c.sendall('You are Connected to Server-A!'.encode('ascii'))
        num1 = c.recv(1024)
        if num1 == b'DONE':
            print('Client at', addr[0], ':', addr[1], 'Disconnected!')
            n = n - 1
            print('Number of Connected Clients:', n)
            break
        num1 = int(num1)
        num2 = int(c.recv(1024))
        num = num1 + num2
        print(num1, ' + ', num2, ' = ', num)
        c.sendall(str(num).encode('ascii'))

    c.close()


n = 0
host = "localhost"
port = 12345
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind((host, port))
print('Socket Binded on port:', port)
s.listen()
print('Socket is Listening...')
while True:
    c, addr = s.accept()
    print('Client at', addr[0], ':', addr[1], 'Requesting Connection!')
    if n < 4:
        threading.Thread(target=sumFunc, args=(c, addr)).start()
    else:
        c.sendall('Server is Busy!\n'.encode('ascii'))
        print('Client at', addr[0], ':', addr[1], 'Connection Denied!')

s.close()
print('Socket Closed!')


