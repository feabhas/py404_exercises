
class Host:
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
        self.services = {}
    
    def __str__(self):
        return '{}:{} services={}'.format(
            self.hostname, self.ip, self.services)

    def add_services(self, services):
        self.services.update(services)
    
    def has_service(self,  service):
        return service in self.services

def main():
    local = Host('127.0.0.0', 'localhost')
    local.add_services({'http':80})
    print(local)
    server = Host('192.168.1.1', 'server')
    server.add_services({'ftp':21, 'https':443})
    print(server)
    print('Local has service http is {}, should be True'.format(local.has_service('http')))
    print('Server has service http is {}, should be False'.format(server.has_service('http')))
    print('Local has service ftp is {}, should be False'.format(local.has_service('ftp')))

if __name__ == '__main__':
    main()
        