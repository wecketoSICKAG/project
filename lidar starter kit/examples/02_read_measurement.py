import socket

HOST = "192.168.0.1"
PORT = 2111

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"\x02sRN LMDscandata\x03")
        data = s.recv(1024)
        if data:
            print(f"Received data: {data}")
except Exception as e:
    print(f"Error: {e}")