import socket

HOST = '127.0.0.1'
PORT = 1044

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message = input("Enter a message: ")
        s.send((message+"\n").encode())

        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                print('Received data chunk from server: ', repr(data))
                message_received += data.decode()
                if message_received.endswith("\n"):
                    print("message received: ", message_received)
                    break
            else:
                print("Connection lost!")
                break
        if not message_received:
            break

print("Client finished")