import socket
import threading

HOST = '127.0.0.1'
PORT = 1050

def receive_messages(client_socket):
    while True:
        message_received = ""
        while True:
            try:
                data = client_socket.recv(32)
                if data:
                    message_received += data.decode()
                    if message_received.endswith("\n"):
                        break
                else:
                    print("Server disconnected")
                    return
            except:
                print("Connection to server lost")
                return
                
        print("\n" + message_received.strip())
        print("Enter a message: ", end='', flush=True)

def send_messages(client_socket):
    while True:
        try:
            message = input("Enter a message: ")
            if message:
                client_socket.send((message + "\n").encode())
        except:
            print("Cannot send message")
            break

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to server")

            receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
            send_thread = threading.Thread(target=send_messages, args=(client_socket,))
            
            receive_thread.start()
            send_thread.start()
            
            receive_thread.join()
            send_thread.join()

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        print("Client finished")

start_client()