"""
command line:

$ python3 setup_heros.py install
"""
import herofuncs

def main():
    root = herofuncs.hero(10)
    print("Hero's root of 10 is {:.4f}".format(root))

if __name__ == '__main__':
    main()
