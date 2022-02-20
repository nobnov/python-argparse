import argparse


parser = argparse.ArgumentParser()
parser.add_argument("v1")
parser.add_argument("--v2")
args = parser.parse_args()

print(args)
