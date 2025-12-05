def load_inventory_data(filename: str = "input.txt"):
    """
    Read the database file and return a list of fresh-ID ranges
    and a list of available ingredient IDs.
    """
    try:
        ranges = []
        food_ids = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if "-" in line:
                    parts = line.split("-")
                    start = int(parts[0])
                    end = int(parts[1])
                    ranges.append([start, end])
                elif line.isdigit():
                    food_ids.append(int(line))
        return ranges, food_ids
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Ensure the file exists.")
        raise

def part1() -> int:
    """
    Count how many available ingredient IDs fall within
    any of the fresh-ID ranges.
    """
    ranges, food_ids = load_inventory_data()
    counter = 0
    for food_id in food_ids:
        for r in ranges:
            if r[0] <= food_id <= r[1]:
                counter += 1
                break
    return counter

def part2() -> int:
    """
    Merge all overlapping fresh-ID ranges and return the total
    number of IDs covered by the merged ranges.
    """
    ranges, _ = load_inventory_data()
    ranges.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end
    merged.append([current_start, current_end])
    total = sum(end - start + 1 for start, end in merged)
    return total

if __name__ == "__main__":
    # Part 1
    result1 = part1()
    print("--- Part 1 ---")
    print(f"Quantity of fresh products available in stock: {result1}")
    # Part 2
    result2 = part2()
    print("\n--- Part 2 ---")
    print(f"The number of all possible different fresh products in the database: {result2}")
