import socket
def can_start_tcp_server(host, port):
    try:
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        server_socket.bind((host, port))
        
        
        server_socket.close()
        return True
    except Exception as e:
        
        return False


host_to_check = '10.66.106.228'
port_to_check = 8080  
if can_start_tcp_server(host_to_check, port_to_check):
    print(f"TCP server can be started on {host_to_check}:{port_to_check}")
else:
    print(f"TCP server cannot be started on {host_to_check}:{port_to_check}")