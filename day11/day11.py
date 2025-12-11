from functools import lru_cache


def read_data(filename="input.txt"):
    """
    Reads input file and returns a list of lines.
    
    Raises:
        FileNotFoundError: if the input file does not exist.
    """
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Ensure the file is present.")
        raise

def part1():
    """
    Counts the number of paths from 'you' to 'out' in a directed graph
    using depth-first search (DFS) without memoization.
    
    Returns:
        result (int): Total number of paths from 'you' to 'out'.
        graph (dict): Graph represented as adjacency lists.
    """
    lines = read_data()
    # Build graph
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        left, right = line.split(":")
        node = left.strip()
        neighbors = right.strip().split()
        graph[node] = neighbors
        
    # DFS to count paths
    def count_paths(graph, start, end):
        paths = 0
        def dfs(node):
            nonlocal paths
            if node == end:
                paths += 1
                return
            for nxt in graph.get(node, []):
                dfs(nxt)
        dfs(start)
        return paths
    
    result = count_paths(graph, "you", "out")
    return result, graph


def part2():
    """
    Counts the number of distinct paths through the graph with multiple segments,
    using DFS with memoization (lru_cache) for efficiency.
    
    Returns:
        result (int): Total number of combined paths from 'svr' to 'out' through specified segments.
        graph (dict): Graph represented as adjacency lists.
    """
    lines = read_data()

    # Build graph
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        left, right = line.split(":")
        node = left.strip()
        neighbors = right.strip().split()
        graph[node] = neighbors

    # DFS with memoization
    def count_paths(graph, start, end)
        @lru_cache(None)
        def dfs(node):
            if node == end:
                return 1
            return sum(dfs(nxt) for nxt in graph.get(node, []))

        return dfs(start)

    # Count all segmented paths
    result = (
        count_paths(graph, "svr", "fft") * count_paths(graph, "fft", "dac") * count_paths(graph, "dac", "out")
        + count_paths(graph, "svr", "dac") * count_paths(graph, "dac", "fft") * count_paths(graph, "fft", "out")
    )
    return result, graph


if __name__ == "__main__":
    # Solve Part 1
    result_part1, _ = part1()
    print("--- Part 1 ---")
    print(f"Number of different paths lead from you to out': {result_part1}")
    # Solve Part 2
    result_part2, _ = part2()
    print("\n--- Part 2 ---")
    print(f"Number of those paths visit both dac and fft: {result_part2}")
