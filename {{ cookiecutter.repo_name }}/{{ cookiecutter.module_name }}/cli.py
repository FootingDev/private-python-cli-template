"""Main CLI"""
import argparse


def say_hello(name):
    print("hello " + name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default="world", help='Say hello to this name.')
    args = parser.parse_args()

    say_hello(args.name)
