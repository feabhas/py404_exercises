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


def main():
    while True:
        query = input('Enter hostname? ')
        if not query:
            break
        result = lookup_addr(query)
        print('{} is {}'.format(query, result if result else 'not found'))

if __name__ == '__main__':
    main()  
