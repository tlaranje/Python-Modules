
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    filename = "lost_archive.txt"
    try:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        with open(filename, "r") as fd:
            fd.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    filename = "classified_vault.txt"
    try:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        with open(filename, "w") as fd:
            fd.write("Test")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    filename = "standard_archive.txt"
    try:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        with open(filename, "r") as fd:
            print(f"SUCCESS: Archive recovered - ``{fd.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
