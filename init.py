import sys
import logging


def read_integers(isTest=False):
    current_day = (sys.argv[0].split('/')[-1].split('.')[0])
    if isTest:
        filename = current_day + "_test.txt"
        logging.warning("*** Using Test Data from " + filename)
    else:
        filename = current_day + "_input.txt"
    with open(filename) as f:
        return [int(x) for x in f]