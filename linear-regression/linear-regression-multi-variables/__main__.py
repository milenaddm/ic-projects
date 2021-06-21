import sys
from getopt import getopt

from linear_regression.linear_regression import linear_regression


def print_usage():
    print("linear-regression-multi-variables usage:\n\npython linear-regression-multi-variables -m <maxepocas> -l <learning-rate>")


def parse_opts(opts):
    maxepocas = None
    learning_rate = None

    for i in range(0, len(opts)):
        if opts[i][0] == "-h":
            print_usage()
            exit()
        elif opts[i][0] == "-m":
            maxepocas = int(opts[i][1])
        elif opts[i][0] == "-l":
            learning_rate = float(opts[i][1][1:])

    if not (maxepocas and learning_rate):
        print("Bad usage!")
        print_usage()
        exit()

    return maxepocas, learning_rate


if __name__ == "__main__":
    opts, args = getopt(sys.argv[1:], "hm:l:")
    maxepocas, learning_rate = parse_opts(opts)

    algoritmo = linear_regression(maxepocas, learning_rate)

    algoritmo.run()
