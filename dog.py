class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"

# Example usage
if __name__ == "__main__":
    my_dog = Dog("Buddy", 3, "Golden Retriever")
    print(my_dog.bark())
    print(my_dog.get_info())