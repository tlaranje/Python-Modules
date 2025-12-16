
def list_comprehension(players):
    print("=== List Comprehension Examples ===")

    high_scores = [p[0] for p in players if p[1] > 2000]
    print(f"High scorers (>2000): {high_scores}")

    scores = [4600, 4600, 3600, 3600, 4300, 4300, 4100, 4100]
    d_s = []
    [d_s.append(s) for s in scores if scores.count(s) > 1 and s not in d_s]
    print(f"Scores doubled: {d_s}")

    active_players = [p[0] for p in players if p[2][0] != ""]
    print(f"Active players: {active_players}")


def dict_comprehension(players):
    print("\n=== Dict Comprehension Examples ===")

    p_scores = {p[0]:p[1] for p in players}
    print(f"Player scores: {p_scores}")

    s_categories = {
        "high": sum(p[1] > 3000 for p in players),
        "medium": sum(2000 < p[1] <= 3000 for p in players),
        "low": sum(p[1] <= 2000 for p in players)}
    print(f"Score categories: {s_categories}")

    ach_count = {p[0]: sum(ach != "" for ach in p[2]) for p in players}
    print(f"Achievement counts: {ach_count}")


def set_comprehension(players):
    print("\n=== Set Comprehension Examples ===")

    unique_players = {p[0] for p in players}
    print(f"Unique players: {unique_players}")

    unique_ach = {ach for p in players for ach in p[2] if ach != ""}
    print(f"Unique achievements: {unique_ach}")

    active_regions = {p[3] for p in players}
    print(f"Active regions: {active_regions}")
""" 
=== Set Comprehension Examples ===
Unique players: {'alice', 'bob', 'charlie', 'diana'}
Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
Active regions: {'north', 'east', 'central'}
 """
def combined_analysis(players):
    print("\n=== Combined Analysis ===")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    players = [("alice", 2300, ["first_kill", "level_10"], "north"),
               ("bob", 1800, ["first_kill", "boss_slayer"], "east"),
               ("charlie", 2150, ["first_kill"], "central"),
               ("diana", 5000, [""], "east")]

    list_comprehension(players)
    dict_comprehension(players)
    set_comprehension(players)
    combined_analysis(players)


""" 
=== Game Analytics Dashboard ===

=== List Comprehension Examples ===
High scorers (>2000): ['alice', 'charlie', 'diana']
Scores doubled: [4600, 3600, 4300, 4100]
Active players: ['alice', 'bob', 'charlie']

=== Dict Comprehension Examples ===
Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
Score categories: {'high': 3, 'medium': 2, 'low': 1}
Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}

=== Set Comprehension Examples ===
Unique players: {'alice', 'bob', 'charlie', 'diana'}
Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
Active regions: {'north', 'east', 'central'}

=== Combined Analysis ===
Total players: 4
Total unique achievements: 12
Average score: 2062.5
Top performer: alice (2300 points, 5 achievements)
"""