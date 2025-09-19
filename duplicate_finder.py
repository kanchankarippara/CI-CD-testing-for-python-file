# duplicate_finder.py

def find_duplicates(input_list):
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
