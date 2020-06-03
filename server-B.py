import socket, threading

def sumFunc(c, addr):
    global n
    print('Client at', addr[0], ':', addr[1], 'Connected!')
    n = n + 1
    print('Number of Connected Clients:', n)
    while True:
        c.sendall('You are Connected to Server-B!'.encode('ascii'))
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


def sockFunc(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((h, p))
    print('Socket Binded on port:', p)
    s.listen()
    print('Socket is Listening on port:', p)
    while True:
        c, addr = s.accept()
        print('Client at', addr[0], ':', addr[1], 'Requesting Connection to port:', p)
        if n < 4:
            threading.Thread(target=sumFunc, args=(c, addr)).start()
        else:
            c.sendall('Server is Busy!\n'.encode('ascii'))
            print('Client at', addr[0], ':', addr[1], 'Connection to port:', p, 'Denied!')

    s.close()
    print('Socket Closed!')

n = 0
host = "localhost"
port = 12345
threading.Thread(target=sockFunc, args=(host, port)).start()
port = 12346
threading.Thread(target=sockFunc, args=(host, port)).start()
