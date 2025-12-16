import time


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def info(self):
        return f"Player {self.name} (level {self.level})"


def game_event_stream(n, players):
    events = ["killed monster", "found treasure", "leveled up"]
    for i in range(n):
        event = events[i % len(events)]
        player = players[i % len(players)]

        yield i + 1, player, event


def stream_analytics(stream):
    t_event = 0
    l_event = 0
    total_events = 0
    high_level_players = 0

    for _, _, event in stream:
        if event == "found treasure":
            t_event += 1
        if event == "leveled up":
            l_event += 1
        if event == "leveled up":
            player.level += 1
        total_events += 1

    for p in players:
        if p.level >= 10:
            high_level_players += 1

    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {t_event}")
    print(f"Level-up events: {l_event}\n")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primes(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    start_time = time.time()
    players = [Player("alice", 5),
               Player("bob", 12),
               Player("charlie", 8)]
    stream = game_event_stream(1000, players)

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    for event_id, player, event in stream:
        if event_id <= 3:
            print(f"Event {event_id}: {player.info()} {event}")
    print("...\n")

    stream_analytics(game_event_stream(1000, players))

    end_time = time.time()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds\n")
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    print(", ".join(str(num) for num in fibonacci(10)))

    print("Prime numbers (first 5):", end=" ")
    print(", ".join(str(p) for p in primes(5)))
