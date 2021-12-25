import sys
import socket
import pickle
from config import Config

HOST = None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Server IP needed: python3 client.py <SERVER IP ADDRESS>")
    HOST = sys.argv[1].strip()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,Config.PORT))
        sock.sendall(b'TESTING DATA FROM CLIENT')
        data = sock.recv(1024)
        #print('Got',repr(data))
        print(pickle.loads(data))