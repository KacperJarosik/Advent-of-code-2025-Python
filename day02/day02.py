MAX_DIGITS = 10 
MIN_DIGITS = 2
def read_data(filename="input.txt"):
    """
    Reads the range data from the file.
    Parses the data into a list of tuples (lower_bound, upper_bound), as INTs.
    """
    data = ""
    try:
        with open(filename, "r") as f:
            data = f.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    parsed_ranges = []
    for range_str in data.split(','):
        lower_str, upper_str = range_str.split('-')
        lower_bound = int(lower_str)
        upper_bound = int(upper_str)
        parsed_ranges.append((lower_bound, upper_bound))
    return parsed_ranges

def part1(ranges: list[tuple[int, int]]) -> int:
    """
    Solves Part 1: Finds and sums all invalid IDs (K repeated exactly 2 times, e.g., KK).
    Formula: ID = K * (10^L + 1), where L is the number of digits in K.
    The maximum ID length is 10 digits, so L ranges from 1 to 5.
    """
    total_sum_of_invalid_ids = 0
    for L in range(MIN_DIGITS // 2, MAX_DIGITS // 2 + 1): 
        multiplier = 10**L + 1
        min_k = 10**(L - 1)
        max_k = 10**L - 1
        for K in range(min_k, max_k + 1):
            invalid_id = K * multiplier
            for lower, upper in ranges:
                if lower <= invalid_id <= upper:
                    total_sum_of_invalid_ids += invalid_id
                    break
    return total_sum_of_invalid_ids

def part2(ranges: list[tuple[int, int]]) -> int:
    """
    Solves Part 2: Finds and sums all invalid IDs (K repeated R >= 2 times, e.g., KKK, KKKK).
    We use a set to ensure each unique invalid ID is counted only once.
    """
    found_invalid_ids = set()
    for L in range(MIN_DIGITS // 2, MAX_DIGITS // 2 + 1):
        min_k = 10**(L - 1)
        max_k = 10**L - 1
        for R in range(2, MAX_DIGITS // L + 1):
            multiplier = sum(10**(L * i) for i in range(R))
            for K in range(min_k, max_k + 1):
                invalid_id = K * multiplier
                if len(str(invalid_id)) > MAX_DIGITS:
                    continue 
                for lower, upper in ranges:
                    if lower <= invalid_id <= upper:
                        found_invalid_ids.add(invalid_id)
                        break
    total_sum_of_invalid_ids = sum(found_invalid_ids)
    return total_sum_of_invalid_ids

if __name__ == "__main__":
    ranges_data = read_data()
    # Solve Part 1
    sum_part1 = part1(ranges_data)
    print(f"--- Part 1: Sum of KK IDs (repeated 2x) ---")
    print(f"What do you get if you sum all invalid IDs: {sum_part1}")
    # Solve Part 2
    sum_part2 = part2(ranges_data)
    print(f"\n--- Part 2: Sum of K...K IDs (repeated >= 2x) ---")
    print(f"What do you get if you sum all invalid IDs: {sum_part2}")
