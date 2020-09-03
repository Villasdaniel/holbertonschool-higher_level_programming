#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    c = len(sys.argv)
    for i in range(1, c):
        s = s + int(sys.argv[i])
    print(s)
