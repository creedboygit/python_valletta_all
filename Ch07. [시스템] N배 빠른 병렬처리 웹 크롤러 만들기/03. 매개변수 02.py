# -*- coding: utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('X', type=int, help='첫번째 숫자는?')
    parser.add_argument('Y', type=int, help='두번째 숫자는?')

    args = parser.parse_args()
    X = args.X
    Y = args.Y
    print("%d 더하기 %d 는? %d" % (X, Y, X + Y))


if __name__ == "__main__":
    main()
