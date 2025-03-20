import socket
import time

HOST = "192.168.0.1"
PORT = 2111

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(b"\x02sEN LMDscandata 1\x03")
        while True:
            try:
                data = s.recv(20048)
                if not data:
                    break
                print(data)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
                break
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Program terminated.")