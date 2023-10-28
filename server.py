import socket
import threading

HOST = '10.42.129.122'
PORT = 12346
HOSTS_FILE = 'hosts.txt'

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address[0]}:{client_address[1]}")

    client_info = client_socket.recv(1024).decode()

    with open(HOSTS_FILE, 'a') as hosts_file:
        hosts_file.write(client_address[0] + '\n')

    print(f"Updated {HOSTS_FILE} with {client_info}")

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Central server is listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
