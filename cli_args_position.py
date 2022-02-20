import argparse


parser = argparse.ArgumentParser()
parser.add_argument("v1", type=int, nargs="+")
parser.add_argument("v2")
args = parser.parse_args()

print(args)
