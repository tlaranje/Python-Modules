
class Player:
    def __init__(self, name):
        self.name = name
        self.ach = set()

    def add_achievements(self, new_ach):
        self.ach = self.ach.union(new_ach)


def unique_achievements(*players):
    unique = set.union(*(p.ach for p in players))
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")


def common_achievements(*players):
    common = set.intersection(*(p.ach for p in players))
    print(f"Common to all players: {common}")


def rare_achievements(*players):
    rare = set()
    for player in players:
        others_union = set.union(*(p.ach for p in players if p != player))
        rare = player.ach.difference(others_union)
        rare.update(rare)
    print(f"Rare achievements (1 player): {rare}")


def alice_bob_common(p1, p2):
    common = p1.ach.intersection(p2.ach)
    print(f"\n{p1.name.capitalize()} vs {p2.name.capitalize()} common: "
          f"{common}")
    print(f"{p1.name.capitalize()} unique: {p1.ach.difference(common)}")
    print(f"{p2.name.capitalize()} unique: {p2.ach.difference(common)}\n")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = Player("alice")
    bob = Player("bob")
    charlie = Player("charlie")

    alice_achs = ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    bob_achs = ["first_kill", "level_10", "boss_slayer", "collector"]
    charlie_achs = ["level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"]

    alice.add_achievements(alice_achs)
    bob.add_achievements(bob_achs)
    charlie.add_achievements(charlie_achs)

    print(f"Player {alice.name} achievements: {alice.ach}")
    print(f"Player {bob.name} achievements: {bob.ach}")
    print(f"Player {charlie.name} achievements: {charlie.ach}")

    print("\n=== Achievement Analytics ===")
    unique_achievements(alice, bob, charlie)
    common_achievements(alice, bob, charlie)
    rare_achievements(alice, bob, charlie)
    alice_bob_common(alice, bob)
