class UpperDemo:
    def convert(self, strings):
        for string in strings:
            yield string.upper()


def hello():
    up = UpperDemo()
    strings = ["Hello", "Xander!"]
    result = " ".join(up.convert(strings))
    print(result)


if __name__ == "__main__":
    hello()
