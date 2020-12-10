#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = (len(sys.argv)-1)
    if length == 0:
        print("{:d}: arguments.".format(0, sys.argv[length]))
        if length == 1:
            print("{:d} argument:\n{:d}: {} ".format(length, length, sys.argv[length]))
        if length > 1:
                print("{:d} arguments:".format(length))

        for i in range(1, (length + 1)):
            print("{:d}: {}".format(i, sys.argv[i]))
