"""
command line:

$ gcc -Wall -shared -o heros.so heros.c
"""
import ctypes as ct
import sys

def main():
    name = './heros.dll' if sys.platform=='win32' else './heros.so'
    heros = ct.cdll.LoadLibrary(name)
    heros.hero.restype = ct.c_double
    heros.hero.argtypes = (ct.c_double,)
    root = heros.hero(ct.c_double(10))
    print("Hero's root of 10 is {:.4f}".format(root))

if __name__ == '__main__':
    main()
