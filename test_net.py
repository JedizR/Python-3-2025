import socket

HOST = '127.0.0.1'
PORT = 2040

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'run successfully')
    data = s.recv(1024)
print('Received', repr(data))
