import socket

class SimpleRedisServer:
    def __init__(self, host='172.20.10.10', port=6379):
        self.host = host
        self.port = port
        self.data = {}

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print(f"Listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address}")
                self.handle_client(client_socket)

    def handle_client(self, client_socket):
        with client_socket:
            while True:
                request = client_socket.recv(1024)
                if not request:
                    break
                response = self.handle_request(request.decode('utf-8'))
                client_socket.sendall(response.encode('utf-8'))

    def handle_request(self, request):
        parts = request.split()
        command = parts[0]

        if command == 'SET':
            key = parts[1]
            value = parts[2]
            self.data[key] = value
            return "+OK\r\n"
        elif command == 'GET':
            key = parts[1]
            value = self.data.get(key, None)
            if value is not None:
                return f"${len(value)}\r\n{value}\r\n"
            else:
                return "$-1\r\n"
        elif command == 'QUIT':
            return "+OK\r\n"
        else:
            return "-ERR Unknown command\r\n"

if __name__ == "__main__":
    server = SimpleRedisServer()
    server.start()
