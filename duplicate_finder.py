"""This module handles user authentication and session management."""
# duplicate_finder.py

def find_duplicates(input_list):
    """
    Scans the given file for duplicate entries and returns a list of duplicates.

    Args:
        file_path (str): Path to the file to be scanned.

    Returns:
        list: A list of duplicate entries found in the file.
    """
    # Your function logic here
    seen = set()
    duplicates = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

if __name__ == "__main__":
    # Example list — you can modify this with your own data
    sample_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
    print("Original list:", sample_list)

    dupes = find_duplicates(sample_list)
    print("Duplicates found:", dupes)
print("Done scanning for duplicates.")



