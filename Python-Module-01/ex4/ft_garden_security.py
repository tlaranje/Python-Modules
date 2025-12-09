
class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, height):
        if height >= 0:
            self.__height = height
        else:
            print("Security: Negative height rejected")

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Security: Negative age rejected")

    def print_info(self):
        print(f"Plant: created: {self.name}")
        print(f"Height updated: {self.get_height()}cm")
        print(f"Age updated: {self.get_age()} days old\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    data = [
        ("Carrot", 30, -1),
        ("Tomato", 50, 30),
        ("Lettuce", 10, 5),
        ("Cucumber", 20, 40),
        ("Potato", 40, 30),
    ]
    all_plants = [SecurePlant(name, height, age) for name, height, age in data]
    for plant in all_plants:
        print(
            f"Current plant: {plant.name} "
            f"({plant.get_height()}cm, {plant.get_age()} days)"
        )
        plant.print_info()

