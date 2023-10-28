import socket
import os


SERVER_HOST = '10.66.106.228'
SERVER_PORT = 12345

def main():
    
    client_info = socket.gethostname()  

    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    
    client_socket.send(client_info.encode())

    
    client_socket.close()

if __name__ == "__main__":
    main()
