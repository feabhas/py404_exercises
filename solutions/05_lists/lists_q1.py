#!/usr/bin/env python3

addr = input('Enter IP addr? ')

fields = addr.split('.')

addr0 = int(fields[0])
addr1 = int(fields[1])
addr2 = int(fields[2])

if 0 <= addr0 < 128:
    cls = 'A'
elif 128 <= addr0 < 192:
    cls = 'B'
elif 192 <= addr0 < 224:
    cls = 'C'
elif 224 <= addr0 < 240:
    cls = 'D'
else:
    cls = 'E'
    
print('{} is class {}'.format(addr, cls))

if addr0 == 10:
    print('private network class A')
elif addr0 == 172 and 16 <= addr1 < 32:
    print('private network class B')
elif (addr0, addr1) == (192, 168):          # addr0==192 and addr1=168
    print('private network class C1')
elif (addr0, addr1, addr2) == (192, 0, 0):  # addr0==192 and addr1=0 and addr2==0:
    print('private network class C2')

