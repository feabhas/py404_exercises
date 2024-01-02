import libfuncs

def main():
    line = input('Enter IP addr? ')
    addr, cls = libfuncs.classify_ip(line)
    print('{}: class {} {}'.format(
        '.'.join(str(n) for n in addr),
        cls,
        'is private' if libfuncs.is_private(addr) else ''))


if (__name__ == "__main__"):
    main()
