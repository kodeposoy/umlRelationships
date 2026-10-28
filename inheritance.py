class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        return "Some generic animal sound"

    def describe((self) -> str:
        return f"{self.name} is {self.age} years old."


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        return "Woof! Woof!"

    def fetch(self, item: str) -> str:
        return f"{self.name} fetched the {item}!"


if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(dog.describe())
    print(dog.make_sound())
    print(dog.fetch("ball"))
