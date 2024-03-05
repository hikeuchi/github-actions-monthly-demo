import os
import math  # Error

import oshoge


def sample_print() -> None:
    print(math.pi)
    print(os.name)
    print("Hello, Python!")


def main() -> None:
    sample_print()
    print("goodbye, Python!")
    print("Hello, Python!")


if __name__ == "__main__":
    main()
