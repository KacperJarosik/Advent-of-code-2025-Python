import copy


def read_input(filename: str = "input.txt") -> list[list[str]]:
    """
    Load the grid of paper rolls from the given input file.
    Each cell contains either '.' (empty) or '@' (paper roll).
    """
    try:
        with open(filename, "r") as f:
            return [list(line.strip()) for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Ensure the file exists.")
        raise

def part1() -> int:
    """
    Count how many rolls of paper can be accessed by a forklift.
    A roll is accessible if fewer than four adjacent cells contain '@'.
    """
    NEIGHBORS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    grid = read_input()
    accessible = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ".":
                continue
            count = 0
            for dr, dc in NEIGHBORS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(row):
                    if grid[nr][nc] == "@":
                        count += 1
            if count < 4:
                accessible += 1
    return accessible

def part2() -> int:
    """
    Repeatedly remove every accessible roll of paper until no more can be removed.
    Return the total number of removed rolls.
    """
    NEIGHBORS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    grid = read_input()
    removed = 0
    changed = True
    while changed:
        changed = False
        new_grid = copy.deepcopy(grid)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == ".":
                    continue
                count_neighbors_papers = 0
                for dr, dc in NEIGHBORS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(row):
                        if grid[nr][nc] == "@":
                            count_neighbors_papers += 1

                if count_neighbors_papers < 4:
                    new_grid[r][c] = "."
                    removed += 1
                    changed = True
        grid = new_grid
    return removed


if __name__ == "__main__":
    # Part 1
    result1 = part1()
    print("--- Part 1 ---")
    print(f"Number of rolls accessible in the initial configuration: {result1}")

    # Part 2
    result2 = part2()
    print("\n--- Part 2 ---")
    print(f"Total number of rolls the forklifts can remove: {result2}")
