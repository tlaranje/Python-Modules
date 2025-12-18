
if __name__ == "__main__":
    filename = "ancient_fragment.txt"
    fd = None

    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print(f"Accessing Storage Vault: {filename}")

        fd = open(filename, "r")

        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(fd.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if fd:
            fd.close()
