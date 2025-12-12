
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    all_plants = [Plant(name, height, age) for name, height, age in plant_data]
    num_plants = 0
    for plant in all_plants:
        plant.print_info()
        num_plants += 1
    print(f"\nTotal plants created: {num_plants}")
