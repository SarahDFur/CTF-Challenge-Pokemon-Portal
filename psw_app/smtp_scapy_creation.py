# from scapy.all import *
#
# def create_smtp_stream(target_ip, target_port):
#     # Create TCP socket
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((target_ip, target_port))
#
#     # Send initial SMTP commands (replace with your desired values)
#     send_command(s, "HELO mydomain.com\r\n")
#     send_command(s, "MAIL FROM:<sender@example.com>\r\n")
#     send_command(s, "RCPT TO:<recipient@example.com>\r\n")
#     send_command(s, "DATA\r\n")
#     send_command(s, "Subject: Test Email\r\n\r\nThis is a test email.\r\n.\r\n")
#     send_command(s, "QUIT\r\n")
#
#     s.close()
#
# def send_command(s, command):
#     s.sendall(command.encode())
#     response = s.recv(1024)
#     print(response.decode())
#
# if __name__ == "__main__":
#     target_ip = "your_smtp_server_ip"
#     target_port = 25
#     create_smtp_stream(target_ip, target_port)


from scapy.all import *

def send_packet_for_wireshark():
    # Create a simple ICMP echo request packet
    packet = IP(dst="127.0.0.1") / TCP()

    # Send the packet
    send(packet, verbose=0)

if __name__ == "__main__":
    send_packet_for_wireshark()