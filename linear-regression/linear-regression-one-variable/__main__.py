import sys
from getopt import getopt

from linear_regression.linear_regression import linear_regression


def print_usage():
    print("linear-regression-one-variable usage:\n\npython linear-regression -m <maxepocas>")


def parse_opts(opts):
    maxepocas = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-m":
            maxepocas = int(opts[i][1])

    if not (maxepocas):
        print("Bad usage!")
        print_usage()
        exit()

    return maxepocas


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hm:")
    maxepocas = parse_opts(opts)

    algoritmo = linear_regression(maxepocas)

    algoritmo.run()
