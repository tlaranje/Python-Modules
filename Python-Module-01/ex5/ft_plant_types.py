
class Plant:
    def __init__(self, plant_type, name, height, age):
        self.plant_type = plant_type
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        if (self.plant_type == "Flower"):
            print(
                f"{self.name} ({self.plant_type}): {self.height}cm, "
                f"{self.age} days, {self.color} color")
        elif (self.plant_type == "Tree"):
            print(
                f"{self.name} ({self.plant_type}): {self.height}cm, "
                f"{self.age} days, {self.diameter}cm diameter")
        elif (self.plant_type == "Vegetable"):
            print(
                f"{self.name} ({self.plant_type}): {self.height}cm, "
                f"{self.age} days, {self.season} harvest")


class Flower(Plant):
    def __init__(self, plant_type, name, height, age, color):
        super().__init__(plant_type, name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, plant_type, name, height, age, diameter):
        super().__init__(plant_type, name, height, age)
        self.diameter = diameter

    def produce_shade(self):
        print(
            f"{self.name} provides {int(self.diameter * 1.56)} "
            "square meters of shade")


class Vegetable(Plant):
    def __init__(self, plant_type, name, height, age, season, nutritional):
        super().__init__(plant_type, name, height, age)
        self.season = season
        self.nutritional = nutritional


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    data = [
        ("Flower", "Rose", 25, 30, "red"),
        ("Flower", "Tulip", 25, 1, "yellow"),
        ("Tree", "Oak", 500, 1875, 50),
        ("Tree", "Pine", 600, 40, 80),
        ("Vegetable", "Tomato", 80, 90, "Summer", "vitamin C"),
        ("Vegetable", "Lettuce", 15, 5, "Spring", "fiber"),
    ]
    plants = []
    for p in data:
        if (p[0] == "Flower"):
            obj = Flower(p[0], p[1], p[2], p[3], p[4])
        elif (p[0] == "Tree"):
            obj = Tree(p[0], p[1], p[2], p[3], p[4])
        elif (p[0] == "Vegetable"):
            obj = Vegetable(p[0], p[1], p[2], p[3], p[4], p[5])
        plants.append(obj)
    for plant in plants:
        if (plant.plant_type == "Flower"):
            plant.print_info()
            plant.bloom()
            print()
        elif (plant.plant_type == "Tree"):
            plant.print_info()
            plant.produce_shade()
            print()
        elif (plant.plant_type == "Vegetable"):
            plant.print_info()
            print(f"{plant.name} is rich in {plant.nutritional}")
            print()
