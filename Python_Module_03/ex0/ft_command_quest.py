import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    args = len(sys.argv)

    if args == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if args > 1:
        print(f"Arguments received: {args - 1}")
        i = 1
        while i < args:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {args}\n")
