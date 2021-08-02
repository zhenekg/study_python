import json
import socket
import re


class ServerSocket:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 9898

    def server_start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(3)
        while True:
            user_conn, addr = server.accept()
            query = user_conn.recv(2048)
            query = json.loads(query.decode("utf-8"))
            if query == "status":
                user_conn.send(json.dumps("connected").encode("utf-8"))
            else:
                text = query['text']
                mask = query['mask']
                result = self.find_in_text(text, mask)
                print(result)
                user_conn.sendall(json.dumps(str(result)).encode("utf-8"))

    @staticmethod
    def find_in_text(text, mask):
        return len(re.findall(mask, text))
