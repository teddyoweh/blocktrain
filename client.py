import socket
import os
import time

SERVER_HOST = '10.42.129.122'
SERVER_PORT = 12346

def main():
    while True:
        try:
            
            client_info = socket.gethostname()  

            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_HOST, SERVER_PORT))

            
            client_socket.send(client_info.encode())

            print(f"Connected to {SERVER_HOST}:{SERVER_PORT} as {client_info}")

            
          

            
            time.sleep(5555560)  
            client_socket.close()

        except Exception as e:
            
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()