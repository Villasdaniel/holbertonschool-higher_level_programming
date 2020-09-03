#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv)
    if c == 1:
        print("0 arguments.")
    elif c == 2:
        print("1 argument:")
    elif c > 2:
        print("{} arguments:".format(c-1))
    for i in range(1, c):
        print("{}: {}".format(i, sys.argv[i]))
