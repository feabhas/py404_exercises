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

    def has_service(self, service):
        return service in self.services

class HostManager:
    def __init__(self):
        self.hosts = []
        
    def __str__(self):
        return '\n'.join(str(host) for host in self.hosts)
    
    def add(self, host, services):
        host.add_services(services)
        self.hosts.append(host)
        
    def find_service(self, service):
        return [host for host in self.hosts if host.has_service(service)]
    
def main():
    manager = HostManager()
    manager.add(Host('127.0.0.0', 'localhost'), {'http': 80, 'https': 443, 'ftp': 21})
    manager.add(Host('192.168.1.1', 'gateway'), {'http': 80})
    manager.add(Host('192.168.1.2', 'host2.local.net'), {'ftp': 21})
    print(manager)
    ftp_hosts = manager.find_service('ftp')
    print('ftp hosts: {}'.format(', '.join(h.hostname for h in ftp_hosts)))
    
if __name__ == '__main__':
    main()
