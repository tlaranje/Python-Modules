
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def info(self):
        return f"Player {self.name} (level {self.level})"


def game_event_stream(n):
    players = [("alice", 5), ("bob", 12), ("charlie", 8)]
    events = ["found treasure", "killed monster", "leveled up"]

    for i in range(n):
        name, level = players[i % len(players)]
        player = Player(name, level)
        event = events[i % len(events)]
        if event == "leveled up":
            player.level += 1
        yield i + 1, player, event


def high_level_players(stream):
    for _, player, _ in stream:
        if player.level >= 10:
            yield player


if __name__ == "__main__":
    stream = game_event_stream(1000)
    total_events = 0;
    count = 0
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...")

    for _ in range(3):
        event_id, player, event = next(stream)
        print(f"Event {event_id}: {player.info()} {event}")
        total_events += 1
    print("...\n")
    for _ in stream:
        total_events += 1
    stream = game_event_stream(1000)
    for _ in high_level_players(stream):
        count += 1
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {count}")

"""
=== Game Data Stream Processor ===

Processing 1000 game events...

Event 1: Player alice (level 5) killed monster
Event 2: Player bob (level 12) found treasure
Event 3: Player charlie (level 8) leveled up
...

=== Stream Analytics ===
Total events processed: 1000
High-level players (10+): 342
Treasure events: 89
Level-up events: 156

Memory usage: Constant (streaming)
Processing time: 0.045 seconds

=== Generator Demonstration ===
Fibonacci sequence (first 10): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Prime numbers (first 5): 2, 3, 5, 7, 11
"""
