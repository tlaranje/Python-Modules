
class GardenManager():
    def __init__(self, name):
            self.stats = GardenManager.GardenStats(self)
            self.name = name
            self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_plants(self, grow):
        print(f"{self.name} is helping all plants grow...")
        total_grow = 0
        for p in self.plants:
            print(f"{p.name} grew {grow}cm")
            total_grow += 1
            p.height += grow
        return total_grow

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def count_by_type(self):
            counts = {'regular': 0, 'flowering': 0, 'prize': 0}
            for plant in self.garden.plants:
                if(plant.plant_type == "Regular"):
                    counts["regular"] += 1
                elif(plant.plant_type == "Flowering"):
                    counts["flowering"] += 1
                elif(plant.plant_type == "Prize"):
                    counts["prize"] += 1
            return counts

        def garden_report(self):
            total_plants = 0
            total_grow = self.garden.grow_plants(1)
            print()
            print(f"=== {self.garden.name}'s Garden Report ===")
            print("Plants in garden:")
            for plant in self.garden.plants:
                if(plant.plant_type == "Regular"):
                    print(f"- {plant.name}: {plant.height}cm")
                elif(plant.plant_type == "Flowering"):
                    print(
                        f"- {plant.name}: {plant.height}cm, "
                        f"{plant.color} flowers (blooming)")
                elif(plant.plant_type == "Prize"):
                    print(
                        f"- {plant.name}: {plant.height}cm, "
                        f"{plant.color} flowers (blooming), "
                        f"Prize points: {plant.prize}")
                total_plants += 1
            print()
            print(f"Plants added: {total_plants}, Total growth: {total_grow}")
            print(my_garden.stats.count_by_type())

class Plant:
    def __init__(self, plant_type, name, height):
        self.plant_type = plant_type
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, plant_type, name, height, color):
        super().__init__(plant_type, name, height)
        self.color = color


class PrizeFlower(Plant):
    def __init__(self, plant_type, name, height, color, prize):
        super().__init__(plant_type, name, height)
        self.color = color
        self.prize = prize


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    my_garden = GardenManager("My Garden")
    data = [
        ("Regular", "Oak Tree", 100),
        ("Flowering", "Rose", 25, "red"),
        ("Prize", "Sunflower", 50, "yellow", 10),
    ]
    for p in data:
        if (p[0] == "Regular"):
            my_garden.add_plant(Plant(p[0], p[1], p[2]))
        elif (p[0] == "Flowering"):
            my_garden.add_plant(FloweringPlant(p[0], p[1], p[2], p[3]))
        elif (p[0] == "Prize"):
            my_garden.add_plant(PrizeFlower(p[0], p[1], p[2], p[3], p[4]))
        print(f"Added {p[1]} to {my_garden.name}")
    print()
    my_garden.stats.garden_report()
