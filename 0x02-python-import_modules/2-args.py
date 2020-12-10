#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    le = (len(sys.argv)-1)

    if le == 0:
        print("{:d}: arguments.".format(0, sys.argv[le]))

    if le == 1:
        print("{:d} argument:".format(1))

    if le > 1:
        print("{:d} arguments:".format(le))

    for i in range(1, (le + 1)):
        print("{:d}: {}".format(i, sys.argv[i]))
