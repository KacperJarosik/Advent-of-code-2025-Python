from functools import lru_cache


def read_schema():
    """Reads teleport schema from input.txt or raises an error if not found."""
    try:
        with open("input.txt", "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Ensure the file is present.")
        raise FileNotFoundError("input.txt missing.")

def part1():
    """Simulates classical tachyon beam splitting"""
    text = [list(line.rstrip("\n")) for line in read_schema()]
    line_index = 1
    result = 0
    for line in text[1:]:
        for i, letter in enumerate(line):
            above = text[line_index - 1][i]
            if above in ("S", "|"):
                if text[line_index][i] == ".":
                    text[line_index][i] = "|"
                elif text[line_index][i] == "^":
                    result += 1
                    if i > 0:
                        text[line_index][i - 1] = "|"
                    if i < len(line) - 1:
                        text[line_index][i + 1] = "|"
        line_index += 1
    new_text = "\n".join("".join(row) for row in text)
    return result, new_text

def part2():
    """Counts the number of possible quantum timelines"""
    grid = [list(line.rstrip("\n")) for line in read_schema()]
    height = len(grid)
    width = len(grid[0])
    for col in range(width):
        if grid[0][col] == "S":
            start = (0, col)
            break
        
    @lru_cache(None)
    def dfs(r, c):
        """Recursive DFS counting all quantum paths."""
        if r == height:
            return 1
        cell = grid[r][c]
        if cell in (".", "S"):
            return dfs(r + 1, c)
        if cell == "^":
            total = 0
            if c > 0:
                total += dfs(r + 1, c - 1)
            if c < width - 1:
                total += dfs(r + 1, c + 1)
            return total
        return dfs(r + 1, c)
    
    return dfs(start[0] + 1, start[1])

if __name__ == "__main__":
    # Solve Part 1
    password_part1, _ = part1()
    print("--- Part 1: ---")
    print(f"The number of times the beam will be split: {password_part1}")
    # Solve Part 2
    password_part2 = part2()
    print("\n--- Part 2: ---")
    print(f"Number of different timelines would a single tachyon particle end up on is: {password_part2}")
