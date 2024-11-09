# game_server.py
import socket
import sys

class GameServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server running on {self.host}:{self.port}")

        try:
            while True:
                # Accept connections from clients
                conn, addr = self.server_socket.accept()
                print(f"Connected by {addr}")
                # Handle client connection here
                data = conn.recv(1024)
                if data:
                    print(f"Received message: {data.decode()}")
                conn.close()

        except KeyboardInterrupt:
            print("\nServer interrupted. Shutting down.")
            self.cleanup()

    def cleanup(self):
        if self.server_socket:
            self.server_socket.close()
            print("Server socket closed.")
        sys.exit(0)  # Exit the program cleanly
