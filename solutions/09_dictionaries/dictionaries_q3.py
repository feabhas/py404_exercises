#!/usr/bin/env python3

HOSTS = {
    'gateway':'192.168.1.1',
    'feabhas':'192.168.1.2',
    'server':'10.0.0.1',
    'mint': '192.168.1.2',
}

def lookup_addr(query):
    if query not in HOSTS:
        return None
    return HOSTS[query]

def lookup_host(query):
    return [host for host, addr in HOSTS.items()
            if addr == query]


def main():
    while True:
        query = input('Enter hostname or address? ')
        if not query:
            break
        if query[0].isdigit():
            result = lookup_host(query)
        else:
            result = lookup_addr(query)
        print('{} is {}'.format(query, result))

if __name__ == '__main__':
    main()  
