
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def print_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Carrot", 30, 10)
    plant1.print_info()
    plant2 = Plant("Tomato", 50, 30)
    plant2.print_info()
    plant3 = Plant("Lettuce", 10, 5)
    plant3.print_info()
