import socket


HOST = '10.66.106.228'  
PORT = 12345     
HOSTS_FILE = 'hosts.txt'  

def main():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Central server is listening on {HOST}:{PORT}")

    while True:
        
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]}")

        
        client_info = client_socket.recv(1024).decode()

        
        with open(HOSTS_FILE, 'a') as hosts_file:
            hosts_file.write(client_info + '\n')

        print(f"Updated {HOSTS_FILE} with {client_info}")

        
        client_socket.close()

if __name__ == "__main__":
    main()
