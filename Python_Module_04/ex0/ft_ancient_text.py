
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        with open("../data-generator-tools/ancient_fragment.txt") as fd:
            print(fd.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    #print(f"Accessing Storage Vault: {}")




"""
=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===

Accessing Storage Vault: ancient\_fragment.txt
Connection established...

RECOVERED DATA:
{[}FRAGMENT 001{]} Digital preservation protocols established 2087
{[}FRAGMENT 002{]} Knowledge must survive the entropy wars
{[}FRAGMENT 003{]} Every byte saved is a victory against oblivion

Data recovery complete. Storage unit disconnected.
"""
