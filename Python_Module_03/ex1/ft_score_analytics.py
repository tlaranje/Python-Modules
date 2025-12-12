import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args = len(sys.argv)

    if args == 1:
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1> <score2> ...\n")
    else:
        try:
            scores_int = [int(arg) for arg in sys.argv[1:]]
            print(f"Scores processed: {scores_int}")
            print(f"Total players: {len(scores_int)}")
            print(f"Total score: {sum(scores_int)}")
            print(f"Average score: {sum(scores_int) / len(scores_int):.2f}")
            print(f"High score: {max(scores_int)}")
            print(f"Low score: {min(scores_int)}")
            print(f"Score range: {max(scores_int) - min(scores_int)}\n")
        except ValueError:
            print("Input arguments can only be numbers, not letters.\n")
