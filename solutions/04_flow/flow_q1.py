#!/usr/bin/env python3

addr = input('Enter IP addr? ')

dot1 = addr.find('.')
part1 = int(addr[0:dot1])
dot1 += 1
dot2 = addr.find('.', dot1)
part2 = int(addr[dot1:dot2])
dot2 += 1
dot3 = addr.find('.', dot2)
part3 = int(addr[dot2:dot3])
dot3 += 1
part4 = int(addr[dot3:])

print(part1, part2, part3, part4)

if 0 <= part1 < 128:
    cls = 'A'
elif 128 <= part1 < 192:
    cls = 'B'
elif 192 <= part1 < 224:
    cls = 'C'
elif 224 <= part1 < 240:
    cls = 'D'
else:
    cls = 'E'
    
print('{} is class {}'.format(addr, cls))
