import socket
import os
import time

SERVER_HOST = '10.66.106.228'
SERVER_PORT = 12345

def main():
    while True:
        try:
            
            client_info = socket.gethostname()  

            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_HOST, SERVER_PORT))

            
            client_socket.send(client_info.encode())

            print(f"Connected to {SERVER_HOST}:{SERVER_PORT} as {client_info}")

            
            client_socket.close()

            
            time.sleep(5555560)  

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()