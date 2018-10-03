#!/usr/bin/env python
def getTerminalSize():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])
def getrandbin(): # get 1 or 0 randomly for the matrix
    import random
    return(random.randint(0, 2))
import time, sys
def matrix(): # this is actually just scrolling binary, not like the strange characters of the matrix
    x, y = getTerminalSize()
    def getLine():
        x, y = getTerminalSize()

        n1 = 0
        v = ''
        while n1 < x:
            x, y = getTerminalSize()
            v += str(getrandbin())
            n1 += 1
        return v
    n2 = 0
    v = ''
    while n2 < y:
        try: 
            t = 0.05
            #global t # uncomment this for the matrix to go a bit faster
            sys.stdout.write('\033[1m\033[32m' + getLine().replace('2', ' ') + '\033[0m\r')
            sys.stdout.flush()
            time.sleep(t)
        except KeyboardInterrupt: #Ctrl+C
            pass
        except EOFError: #Ctrl+D
            break

matrix()
