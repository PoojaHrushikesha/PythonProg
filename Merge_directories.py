def merge_using_union(dict1, dict2):
    # Merges dict2 into dict1; values from dict2 override if keys overlap
    merged = dict1 | dict2  # Requires Python 3.9+
    return merged

def merge_using_update(dict1, dict2):
    merged = dict1.copy()  # Make a copy to avoid modifying the original
    merged.update(dict2)   # Updates dict1 with dict2's keys and values
    return merged

def merge_with_conflict_handling(dict1, dict2):
    # Custom merge: if keys overlap, combine values in a list
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = [merged[key], value]
        else:
            merged[key] = value
    return merged

def main():
    # Define two sample dictionaries
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 20, 'd': 4}

    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)

    print("\nMerged using '|' operator (Python 3.9+):")
    print(merge_using_union(dict1, dict2))

    print("\nMerged using update():")
    print(merge_using_update(dict1, dict2))

    print("\nMerged with conflict handling (combine values):")
    print(merge_with_conflict_handling(dict1, dict2))

if __name__ == "__main__":
    main()
