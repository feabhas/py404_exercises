#!/usr/bin/env python3
"""
Read single character - run from command line not IDE
"""

try:
    import sys, termios

    def getchar():
        fd = sys.stdin.fileno()
        oldattr = termios.tcgetattr(fd)
        try:
            newattr = oldattr.copy()
            newattr[3] &= ~(termios.ICANON|termios.ECHO)
            termios.tcsetattr(fd, termios.TCSANOW, newattr)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldattr)
        return ch

except ImportError:
    try:
        import msvcrt
        getchar = msvcrt.getch

    except ImportError:
        raise OSError('Cannot provide getchar function on this OS')

sys.stdout.write('Press a key? ')
sys.stdout.flush()
char = getchar()
print('\nYou pressed {}'.format(char))
