from itertools import combinations, pairwise


def read_data(filename="input.txt"):
    """Reads coordinates from a file and returns them as a list of tuples (x, y)."""
    try:
        with open(filename, "r") as f:
            return [tuple(map(int, line.strip().split(","))) for line in f]
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Ensure the file is present.")
        raise

def part1(coords):
    """Finds the maximum area of any rectangle formed by pairs of points."""
    max_area = 0
    for (x, y), (u, v) in combinations(coords, 2):
        x, u = sorted((x, u))
        y, v = sorted((y, v))
        size = (u - x + 1) * (v - y + 1)
        max_area = max(max_area, size)
    return max_area

def part2(coords):
    """Finds the largest area of any rectangle you can make using only red and green tiles."""
    max_area = 0
    for (x, y), (u, v) in combinations(coords, 2):
        x, u = sorted((x, u))
        y, v = sorted((y, v))
        size = (u - x + 1) * (v - y + 1)

        for (p, q), (r, s) in pairwise(coords + [coords[0]]):
            p, r = sorted((p, r))
            q, s = sorted((q, s))
            if all((x < r, u > p, y < s, v > q)):
                break
        else:
            max_area = max(max_area, size)

    return max_area


if __name__ == "__main__":
    coordinates = read_data()
    # Solve Part 1
    max_area_part1 = part1(coordinates)
    print("--- Part 1: ---")
    print(f"The largest area of any rectangle you can make: {max_area_part1}")
    # Solve Part 2
    max_area_part2 = part2(coordinates)
    print("\n--- Part 2: ---")
    print(f"The largest area of any rectangle you can make using only red and green tiles: {max_area_part2}")
