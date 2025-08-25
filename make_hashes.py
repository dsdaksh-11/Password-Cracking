def clean_hashes(filename):
    """
    Reads a file containing 'username:hash' lines
    and overwrites it with only the hashes.
    """
    try:
        with open(filename, "r") as infile:
            lines = infile.readlines()

        with open(filename, "w") as outfile:
            for line in lines:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    outfile.write(parts[1] + "\n")

        print(f"[+] Cleaned {filename} → now contains only hashes.")

    except FileNotFoundError:
        print(f"[!] File {filename} not found.")
    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    clean_hashes("weak_hashes.txt")
    clean_hashes("strong_hashes.txt")
