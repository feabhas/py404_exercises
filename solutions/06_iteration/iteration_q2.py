
addr_list = []
while True:
    addr = input('IP addr (blank to stop)? ').strip()
    if not addr:
        break
    addr_list.append(addr)

for addr in addr_list:
    fields = [int(s) for s in addr.split('.')]
        
    if 0 <= fields[0] < 128:
        cls = 'A'
    elif 128 <= fields[0] < 192:
        cls = 'B'
    elif 192 <= fields[0] < 224:
        cls = 'C'
    elif 224 <= fields[0] < 240:
        cls = 'D'
    else:
        cls = 'E'
        
    print('{} is class {}'.format(addr, cls))
    
    if fields[0] == 10:
        print('private network class A')
    elif fields[0] == 172 and 16 <= fields[1] < 32:
        print('private network class B')
    elif fields[0:2] == [192, 168]:
        print('private network class C1')
    elif fields[0:3] == [192, 0, 0]:
        print('private network class C2')
