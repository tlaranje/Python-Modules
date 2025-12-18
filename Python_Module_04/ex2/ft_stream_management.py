import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    sts_report = input("Input Stream active. Enter status report: ")

    print(f"\n{{[}}STANDARD{{]}} Archive status from {arch_id}: {sts_report}",
          file=sys.stdout)
    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("{[}STANDARD{]} Data transmission complete\n",
          file=sys.stdout)
    print("Three-channel communication test successful.",
          file=sys.stdout)
