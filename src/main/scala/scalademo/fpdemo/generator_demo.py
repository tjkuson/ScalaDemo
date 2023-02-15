from math import prod


def main():
    result = prod(n * 2 for n in range(1, 11) if n % 2 == 0)
    assert result == 122880


if __name__ == "__main__":
    main()
