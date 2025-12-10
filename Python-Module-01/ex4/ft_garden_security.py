
class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}")
        print(f"Height updated: {self.get_height()}cm [OK]")
        print(f"Age updated: {self.get_age()} days [OK]\n")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print(f"Security: Negative age rejected for {self.name}\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    data = [
        ("Rose", 25, 30),
    ]
    all_plants = [SecurePlant(name, height, age) for name, height, age in data]
    for plant in all_plants:
        plant.set_height(-5)
        print(
            f"Current plant: {plant.name} "
            f"({plant.get_height()}cm, {plant.get_age()} days)\n")
