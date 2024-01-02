
class Host:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def __str__(self):
        return '{}:{}'.format(
            self.hostname, self.ip)

def main():
    local = Host('127.0.0.0', 'localhost')
    print(local)
    server = Host('192.168.1.1', 'server')
    print(server)

if __name__ == '__main__':
    main()
