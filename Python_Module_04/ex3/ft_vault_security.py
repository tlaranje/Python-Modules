
if __name__ == "__main__":
    filename = "classified_data.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    with open(filename, "r") as fd:
        print(fd.read())

    print("SECURE PRESERVATION:")
    with open(filename, "w") as fd:
        fd.write("{[}CLASSIFIED{]} New security protocols archived\n")
        print("{[}CLASSIFIED{]} New security protocols archived")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")
