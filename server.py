import socket
import threading

def run_server():
    server_ip = "YOUR SERVER IP" 
    port = 8000

    client_threads = []  # Lista para guardar los hilos de clientes
    client_sockets = []  # Lista para guardar los sockets de clientes

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((server_ip, port))
        server.listen()
        server.settimeout(1.0)
        print(f"Server listening on {server_ip}:{port}")

        while True:
            try:
                client_socket, addr = server.accept()
                print(f"Accepted connection from {addr[0]}:{addr[1]}")
                thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
                thread.start()
                client_threads.append(thread)
                client_sockets.append(client_socket)
            except socket.timeout:
                continue
    except KeyboardInterrupt:
        print("\n Server shutting down...")
    finally:
        server.close()
        
        for cs in client_sockets:
            try:
                cs.shutdown(socket.SHUT_RDWR)
                cs.close()
            except Exception:
                pass
        for t in client_threads:
            t.join()
        print("All clients were disconnected. Server Closed.")
    
def handle_client(client_socket, addr):
    try:
        while True:
            try:
                request = client_socket.recv(1024).decode('utf-8')
            except OSError as e:
                if hasattr(e, 'winerror') and e.winerror == 10038:
                    break
                else:
                    raise
            if request.lower() == "close connection":
                client_socket.send("Connection closed".encode('utf-8'))
                break
            print(f"Received: {request} from:{addr[0]}:{addr[1]}")
            print("="*40)
            response = "Accepted"
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed.")

run_server()
