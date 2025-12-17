import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args = len(sys.argv)

    if args == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...\n")
    else:
        try:
            scores = [int(arg) for arg in sys.argv[1:]]
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores):.1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}\n")
        except ValueError:
            print("Input arguments can only be numbers, not letters.\n")
