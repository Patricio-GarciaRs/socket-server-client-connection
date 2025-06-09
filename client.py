import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "YOUR_SERVER_IP" 
    server_port = 8000

    client.connect((server_ip, server_port))

    try:
        while True:
            msg = input("Enter message (or 'close connection' to exit): ")
            client.send(msg.encode('utf-8'))

            response = client.recv(1024)
            response = response.decode('utf-8')

            if response.lower() == "connection closed":
                break

            print (f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed.")

run_client()