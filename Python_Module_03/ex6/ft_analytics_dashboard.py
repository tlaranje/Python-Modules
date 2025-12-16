
def list_comprehension():
    print("=== List Comprehension Examples ===")

    players = [("alice", 3000, "first_kill"),
               ("charlie", 4000, "first_kill"),
               ("diana", 5000, ""),
               ("bob", 2000, "first_kill")]

    high_scores = [name for name, score, _ in players if score > 2000]
    print(f"High scorers (>2000): {high_scores}")

    scores = [4600, 4600, 3600, 3600, 4300, 4300, 4100, 4100]
    d_s = []
    [d_s.append(s) for s in scores if scores.count(s) > 1 and s not in d_s]
    print(f"Scores doubled: {d_s}")

    active_players = [name for name, _, a in players if a]
    print(f"Active players: {active_players}")


def dict_comprehension():
    print("\n=== Dict Comprehension Examples ===")


def set_comprehension():
    print("\n=== Set Comprehension Examples ===")


def combined_analysis():
    print("\n=== Combined Analysis ===")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analysis()
