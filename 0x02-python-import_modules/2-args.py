#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    argc = len(argv) - 1
    print("{:d} {}{}".format(argc, "argument" if argc == 1 else "arguments",
                             ":" if argc else "."))
    if argc:
        out = [print("{:d}: {}".format(i + 1, argv[i + 1])) for i in
               range(argc)]
