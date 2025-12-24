#!/usr/bin/env python3
import socket
import json


def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 12345))
        server_socket.listen(1)

        conn, addr = server_socket.accept()

        data = conn.recv(1024).decode("utf-8")
        dictionary = json.loads(data)

        print("Received Dictionary from Client:")
        print(dictionary)

        conn.close()
        server_socket.close()

    except Exception:
        pass


def send_data(data):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", 12345))

        serialized_data = json.dumps(data)
        client_socket.sendall(serialized_data.encode("utf-8"))

        client_socket.close()

    except Exception:
        pass
