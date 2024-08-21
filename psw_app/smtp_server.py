import socket
from scapy.all import *

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        command = data.decode().strip()
        print(f"Received: {command}")

        # Basic command handling
        if command == "HELO":
            response = "250 Hello, client\r\n"
        elif command == "MAIL FROM:<sender@example.com>":
            response = "250 Ok\r\n"
        elif command == "RCPT TO:<recipient@example.com>":
            response = "250 Ok\r\n"
        elif command == "DATA":
            response = "354 Start mail input; end with <CRLF>.<CRLF>\r\n"
            conn.sendall(response.encode())
            while True:
                data = conn.recv(1024)
                if data.endswith(b".\r\n"):
                    break
            response = "250 Ok\r\n"
        elif command == "QUIT":
            response = "221 Bye\r\n"
            conn.sendall(response.encode())
            break
        else:
            response = "500 Command not recognized\r\n"
        conn.sendall(response.encode())

    conn.close()


def smtp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            handle_client(conn, addr)


if __name__ == "__main__":
    smtp_server('', 25)
