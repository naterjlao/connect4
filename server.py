import socket
import pickle
from config import Config
from logic import Board

HOST = "0.0.0.0"

if __name__ == "__main__":
    board = Board()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST,Config.PORT))
        sock.listen()
        conn, addr = sock.accept()
        with conn:
            print("Connection established: ", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Got", repr(data))
                conn.sendall(pickle.dumps(str(board)))