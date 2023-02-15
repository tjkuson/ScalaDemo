"""
Subclass polymorphism in Python.
"""


class Animal:
    """Abstract class for animals."""

    def process(self):
        """Virtual method to be implemented by subclasses."""
        raise NotImplementedError


class Human(Animal):
    """Human class."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def process(self):
        return f"Hello, my name is {self.name}"


class Dog(Animal):
    """Dog class."""

    def __init__(self, is_big):
        super().__init__()
        self.is_big = is_big

    def process(self):
        return "Woof" if self.is_big else "Yip"


class Cat(Animal):
    """Cat class."""

    def __init__(self):
        super().__init__()

    def process(self):
        return "Meow"


def main():
    """Demonstrate subclass polymorphism."""
    animals = [Human("John"), Dog(True), Dog(False), Cat(), Animal()]
    for animal in animals:
        # Animal.process() is not implemented, so it will raise an exception.
        print(animal.process())


if __name__ == "__main__":
    main()
