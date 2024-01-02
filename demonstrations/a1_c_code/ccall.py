import ctypes as ct
import sys

def main():
    name = './clib.dll' if sys.platform=='win32' else './clib.so'
    lib = ct.cdll.LoadLibrary(name)

    lib.show()

    lib.adder.restype = ct.c_double
    lib.adder.argtypes = (ct.c_double, ct.c_int, ct.c_void_p)

    dpar = ct.c_double(3.5)
    refpar = ct.c_int()
    answer = lib.adder(dpar, 3, ct.byref(refpar))
    print('3.5 + 3 = {} and {}'.format(answer, refpar.value))

    src = (ct.c_double*10)(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    results = (ct.c_double*10)()
    lib.square(results, src, 10)
    print(list(results))

if __name__ == '__main__':
    main()
