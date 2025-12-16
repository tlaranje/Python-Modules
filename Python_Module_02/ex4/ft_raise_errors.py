
def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health based on name, water level, and sunlight hours."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """Run tests for the check_plant_health function with various inputs."""
    print("=== Garden Plant Health Checker ===\n")

    tests = [
        ("Testing good values...", "tomato", 5, 5),
        ("Testing empty plant name...", "", 5, 5),
        ("Testing bad water level...", "tomato", 15, 5),
        ("Testing bad sunlight hours...", "tomato", 5, 0),
    ]

    for description, name, water, sun in tests:
        print(description)
        try:
            result = check_plant_health(name, water, sun)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
        print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
