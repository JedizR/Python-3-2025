import socket
import sys
import threading

HOST = '0.0.0.0'
PORT = 1050

class ChatServer:
    def __init__(self):
        self.clients = []
        self.lock = threading.Lock()
        
    def handle_client(self, client_socket, client_address):
        print(f'New connection from {client_address}')
        
        while True:
            message_received = ""
            while True:
                try:
                    data = client_socket.recv(32)
                    if data:
                        print(f'Received data chunk from {client_address}: {repr(data)}')
                        message_received += data.decode()
                        if message_received.endswith("\n"):
                            break
                    else:
                        raise ConnectionError("Connection lost")
                except:
                    print(f"Client {client_address} disconnected")
                    with self.lock:
                        self.clients.remove(client_socket)
                    client_socket.close()
                    return

            if message_received:
                formatted_message = f"Client {client_address}: {message_received}"
                print(formatted_message)
                self.broadcast_message(formatted_message, client_socket)

    def broadcast_message(self, message, sender_socket):
        with self.lock:
            for client in self.clients:
                if client != sender_socket:
                    try:
                        client.send(message.encode())
                    except:
                        self.clients.remove(client)
                        client.close()

    def start_server(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created")
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print("Socket bound and listening")

            while True:
                client_socket, client_address = server_socket.accept()
                with self.lock:
                    self.clients.append(client_socket)
                
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address)
                )
                client_thread.start()

        except Exception as e:
            print(f"Server error: {e}")
        finally:
            server_socket.close()
            print("Server finished")

chat_server = ChatServer()
chat_server.start_server()