
import socket
import json


class ClientSocket:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 9898

    def client_send(self, query):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.sendall(json.dumps(query).encode("utf-8"))
        data_recv = json.loads(client.recv(2048).decode("utf-8"))
        client.close()
        return data_recv
