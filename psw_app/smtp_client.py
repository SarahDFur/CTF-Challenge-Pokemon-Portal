import socket

def smtp_client(host, port, sender, recipient, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # Basic commands
        s.sendall(b"HELO mydomain.com\r\n")
        s.recv(1024)
        s.sendall(f"MAIL FROM:<{sender}>\r\n".encode())
        s.recv(1024)
        s.sendall(f"RCPT TO:<{recipient}>\r\n".encode())
        s.recv(1024)
        s.sendall(b"DATA\r\n")
        s.recv(1024)
        s.sendall(f"Subject: Test Email\r\n\r\n{message}\r\n.\r\n".encode())
        s.recv(1024)
        s.sendall(b"QUIT\r\n")
        s.recv(1024)

if __name__ == "__main__":
    smtp_client("localhost", 25, "sender@example.com", "recipient@example.com",
                """
                Your friend is in danger ! ! !
                You must find the decryption key quickly:
                Salted__{jÛ/ÅÞÕxR4öl[¶‘>†CéœÌ[iP9Ñ‡8`!!0 
                """)

# Encrypted password will be inside the {message}
# The decryption key is inside the PDF file :-)
# The dec password == pokemon_unite