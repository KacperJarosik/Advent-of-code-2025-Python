def part1() -> int:
    """
    Apply the operations column-wise across all rows of numbers:
    + for addition, * for multiplication.
    Returns the sum of the resulting row.
    """
    def read_data(filename: str = "input.txt"):
        """
        Read the input file and return:
        - a list of integer lists (all lines except the last),
        - a list of operations from the last line.
        """
        try:
            with open(filename, "r") as f:
                lines = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Error: '{filename}' not found. Ensure the file is present.")
            raise
        numbers = [[int(num) for num in line.split()] for line in lines[:-1]]
        operations = lines[-1].split()
        return numbers, operations
    
    numbers, operations = read_data()
    results = numbers[0].copy()
    for row in numbers[1:]:
        for i, op in enumerate(operations):
            if op == "+":
                results[i] += row[i]
            elif op == "*":
                results[i] *= row[i]
    return sum(results)

def part2(filename: str = "input.txt") -> int:
    """
    Parse the file as column-aligned mini-problems:
    - Each vertical block of digits+operator is considered one problem.
    - Operator is in the last row.
    - The digits above each operator form integers (by column).
    Returns the sum of all solved problems.
    """
    with open(filename, "r") as f:
        raw = [line.rstrip("\n") for line in f]
    # Height without operator row
    height = len(raw) - 1
    ops_row = raw[-1]
    # Normalize width
    width = max(len(line) for line in raw)
    raw = [line.ljust(width) for line in raw]
    # Separate continuous column blocks (problems)
    problems = []
    current = []
    for c in range(width):
        is_gap = all(raw[r][c] == " " for r in range(height + 1))
        if is_gap:
            if current:
                problems.append(current)
                current = []
        else:
            current.append(c)
    if current:
        problems.append(current)
    total = 0
    # Process each column-defined problem
    for cols in problems:
        # Find operator in the operator row
        operator = None
        for c in cols:
            if ops_row[c] in "+*":
                operator = ops_row[c]
                break
        # Extract numbers formed by digits in each column
        nums = []
        for c in cols:
            digits = [raw[r][c] for r in range(height) if raw[r][c].isdigit()]
            if digits:
                nums.append(int("".join(digits)))
        # Compute the result of the problem
        if operator == "+":
            result = sum(nums)
        else:
            result = 1
            for x in nums:
                result *= x
        total += result
    return total


if __name__ == "__main__":
    print("--- Part 1 ---")
    print(f"Cephalopod math homework version 1: {part1()}")
    print("\n--- Part 2 ---")
    print(f"Cephalopod math homework version 2: {part2()}")
