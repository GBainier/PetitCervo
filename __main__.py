import argparse


def main(args):
    print(args.neurons)
    print(args.verbose)
    return 0

# entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create and simulate a small brain.")
    parser.add_argument("-n", "--neurons", type=int, help="Number of neurons.")
    parser.add_argument("-v", "--verbose", help="Print additional information.", action="store_true")
    args = parser.parse_args()
    main(args)