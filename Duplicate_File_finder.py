import os
import hashlib
import sys

def hash_file(path, block_size=65536):
    """Return SHA-256 hash of the file."""
    sha = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while chunk = f.read(block_size):
                sha.update(chunk)
        return sha.hexdigest()
    except (PermissionError, FileNotFoundError):
        return None


def scan_directory(start_path):
    """Walk through directory recursively and hash each file."""
    file_hash_map = {}  # hash → list of files

    print("\nScanning for files...\n")

    for root, _, files in os.walk(start_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            file_hash = hash_file(file_path)
            if not file_hash:
                continue

            file_hash_map.setdefault(file_hash, []).append(file_path)

    return file_hash_map


def show_duplicates(file_hash_map):
    """Print duplicate files found."""
    duplicate_groups = [
        paths for paths in file_hash_map.values()
        if len(paths) > 1
    ]

    if not duplicate_groups:
        print("\n✔ No duplicates found.\n")
        return []

    print("\n====== DUPLICATE FILES FOUND ======\n")

    for i, group in enumerate(duplicate_groups, start=1):
        print(f"Group {i}:")
        for p in group:
            print(f"  - {p}")
        print()

    return duplicate_groups


def delete_duplicates(duplicate_groups):
    """Allow user to delete duplicates interactively."""
    print("\nDo you want to delete duplicate files?")
    choice = input("(y/n): ").strip().lower()

    if choice != "y":
        print("No files deleted.")
        return

    for group in duplicate_groups:
        # Keep the first file, delete the rest
        keep = group[0]
        delete_list = group[1:]

        print(f"\nKeeping: {keep}")
        print("Deleting duplicates:")

        for file_path in delete_list:
            try:
                os.remove(file_path)
                print(f"  ✔ Deleted: {file_path}")
            except PermissionError:
                print(f"  ✖ Permission denied: {file_path}")
            except Exception as e:
                print(f"  ✖ Could not delete {file_path}: {e}")

    print("\n✔ Duplicate cleanup completed.\n")


def main():
    print("\n====== DUPLICATE FILE FINDER ======\n")

    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        start_path = input("Enter directory to scan: ").strip()

    if not os.path.isdir(start_path):
        print("Error: Not a valid directory.")
        return

    file_hash_map = scan_directory(start_path)
    duplicate_groups = show_duplicates(file_hash_map)

    if duplicate_groups:
        delete_duplicates(duplicate_groups)


if __name__ == "__main__":
    main()
