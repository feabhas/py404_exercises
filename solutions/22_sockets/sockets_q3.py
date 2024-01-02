import socket
import random
 
HOST = ''   # All available interfaces
PORT = 8883 # Arbitrary non-privileged port

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp:
        tcp.bind((HOST, PORT))
        tcp.listen(2)
        thost, tport = tcp.getsockname()
        print('listening on {}:{}'.format(thost, tport))
        while True:
            conn = None
            try:
                conn, addr = tcp.accept()
                request = conn.recv(1024)
                print('Received {} from {}:{}'.format(request, addr[0],addr[1]))
                count, limit = [int(n) for n in request.decode('utf8').split(',')]
                for _ in range(count):
                    n = random.randrange(limit)
                    conn.sendall(str(n).encode('utf8')+b'\r\n')
            finally:
                if conn:
                    conn.close()

if __name__ == '__main__':
    main() 
    