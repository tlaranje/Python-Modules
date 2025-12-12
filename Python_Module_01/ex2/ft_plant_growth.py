
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def age_plant(self, age):
        self.age += age

    def grow_plant(self, grow):
        self.height += grow


if __name__ == "__main__":
    grow = 0
    time_age = 0
    plant_data = [
        ("Rose", 25, 30),
    ]
    all_plants = [Plant(name, height, age) for name, height, age in plant_data]
    print("=== Day 1 ===")
    for plant in all_plants:
        plant.print_info()
    print()
    for day in range(2, 8):
        print(f"=== Day {day} ===")
        grow += 1
        time_age += 1
        for plant in all_plants:
            plant.grow_plant(1)
            plant.age_plant(1)
            plant.print_info()
        print()
    print(f"Growth this week: +{grow}cm")
