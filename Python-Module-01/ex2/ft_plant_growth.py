
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
    print("=== Garden Plant Registry ===")
    grow = 0
    time_age = 0
    plant_data = [
        ("Carrot", 30, 10),
        ("Tomato", 50, 30),
        ("Lettuce", 10, 5),
    ]
    all_plants = [Plant(name, height, age) for name, height, age in plant_data]
    for plant in all_plants:
        plant.print_info()
    print("\n=== Week Grow Status ===")
    for day in range(1, 8):
        print(f"Day {day}")
        grow += 1
        time_age += 1
        for plant in all_plants:
            plant.grow_plant(1)
            plant.age_plant(1)
            plant.print_info()
        print()
    print(f"Plants growth {grow}cm and age {time_age} days this week")
