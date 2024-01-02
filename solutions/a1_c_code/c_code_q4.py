"""
command line:

$ swig -python heroswig.i
$ gcc -c heros.c heroswig_wrap.c -fPIC -I/usr/include/python3.5
$ ld -shared heros.o heroswig_wrap.o -o _heroswig.so
"""
import heroswig

def main():
    root = heroswig.hero(10)
    print("Hero's root of 10 is {:.4f}".format(root))

if __name__ == '__main__':
    main()
