
def list_comprehension(players, NAME, SCORE, ACH):
    print("=== List Comprehension Examples ===")

    high_scores = [p[NAME] for p in players if p[SCORE] > 2000]
    print(f"High scorers (>2000): {high_scores}")

    scores = [4600, 4600, 3600, 3600, 4300, 4300, 4100, 4100]
    d_s = sorted({s for s in scores if scores.count(s) > 1})
    print(f"Scores doubled: {d_s}")

    active_players = [p[NAME] for p in players if p[ACH][0] != ""]
    print(f"Active players: {active_players}")


def dict_comprehension(players, NAME, SCORE, ACH):
    print("\n=== Dict Comprehension Examples ===")

    p_scores = {p[NAME]: p[SCORE] for p in players}
    print(f"Player scores: {p_scores}")

    s_categories = {
        "high": sum(p[SCORE] >= 2300 for p in players),
        "medium": sum(2000 <= p[SCORE] < 2300 for p in players),
        "low": sum(p[SCORE] < 2000 for p in players)}
    print(f"Score categories: {s_categories}")

    ach_count = {p[NAME]: sum(ach != "" for ach in p[ACH]) for p in players}
    print(f"Achievement counts: {ach_count}")


def set_comprehension(players, NAME, ACH, REGION):
    print("\n=== Set Comprehension Examples ===")

    unique_players = sorted({p[NAME] for p in players})
    print(f"Unique players: {unique_players}")

    unique_ach = sorted({a for p in players for a in p[ACH] if a != ""})
    print(f"Unique achievements: {unique_ach}")

    active_regions = sorted({p[REGION] for p in players})
    print(f"Active regions: {active_regions}")


def combined_analysis(players, NAME, SCORE, ACH):
    print("\n=== Combined Analysis ===")

    total_players = sum(p[NAME] != "" for p in players)
    print(f"Total players: {total_players}")

    total_unique_ach = {a for p in players for a in p[ACH] if a != ""}
    count_ach = len(total_unique_ach)
    print(f"Total unique achievements: {count_ach}")

    avg_score = sum(p[SCORE] for p in players) / total_players
    print(f"Average score: {avg_score}")

    max_score = max(p[SCORE] for p in players)
    name = [p[NAME] for p in players if p[SCORE] == max_score][0]
    count_a = len({a for p in players for a in p[ACH]
                   if p[SCORE] == max_score and a != ""})
    print(f"Top performer: {name} ({max_score} points, "
          f"{count_a} achievements)\n")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    name = 0
    score = 1
    ach = 2
    region = 3

    players = [
        ("alice", 2300, ["first_kill", "level_10", "collector"], "north"),
        ("bob", 1800, ["first_kill", "boss_slayer"], "east"),
        ("charlie", 2150, ["first_kill"], "central"),
        ("diana", 2100, [""], "east")]

    list_comprehension(players, name, score, ach)
    dict_comprehension(players, name, score, ach)
    set_comprehension(players, name, ach, region)
    combined_analysis(players, name, score, ach)
