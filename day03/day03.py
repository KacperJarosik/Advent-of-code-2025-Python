def read_batteries_banks(filename: str = "input.txt") -> list[str]:
    """
    Reads all lines from the given input file and returns a list of stripped lines.
    """
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Ensure the file exists.")
        raise

def part1(lines: list[str]) -> int:
    """
    Part 1:
    For each line (battery bank), find the largest digit and the largest digit that occurs *after*
    the largest one. Combine them into a two-digit number, accumulate the sum.
    """
    joltages = []
    for line in lines:
        if not line:
            continue
        first_digit = '0'
        first_pos = 0
        for i, ch in enumerate(line[:-1]):
            if ch > first_digit:
                first_digit = ch
                first_pos = i
        second_digit = max(line[first_pos + 1:], default='1')
        joltages.append(int(first_digit + second_digit))
    return sum(joltages)

def part2(lines: list[str], required_length: int = 12) -> int:
    """
    Part 2:
    Given each numeric string (battery bank), reduce it to exactly 'required_length' digits
    while preserving maximum lexicographic value using a monotonic decreasing stack.
    """
    total = 0
    for line in lines:
        digits = [int(c) for c in line]
        drop = len(digits) - required_length
        stack = []
        for d in digits:
            while stack and drop > 0 and stack[-1] < d:
                stack.pop()
                drop -= 1
            stack.append(d)
        final_digits = stack[:required_length]
        total += int("".join(map(str, final_digits)))
    return total


if __name__ == "__main__":
    data = read_batteries_banks()
    # Part 1
    result1 = part1(data)
    print("--- Part 1: 2 digits battery banks ---")
    print(f"The sum of joltages is: {result1}")
    # Part 2
    result2 = part2(data)
    print("\n--- Part 2: 12 digits battery banks ---")
    print(f"The sum of joltages is: {result2}")
