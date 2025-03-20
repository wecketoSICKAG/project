import socket

HOST = "192.168.0.1"
PORT = 2111

try:
    with socket.create_connection((HOST, PORT)) as s:
        print("Connecting to the LiDAR device...")
        s.sendall(b"\x02sRN DItype\x03")
        print("Device type request sent.")
        data = s.recv(1024).decode('utf-8')
        print(f"Received device type: {data}" if data else "No data received.")
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Program terminated.")