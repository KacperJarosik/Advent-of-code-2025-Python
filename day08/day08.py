from itertools import combinations


def read_schema():
    """
    Reads data from the 'input.txt' file and returns a list of coordinates
    as lists of integers [x, y, z].

    Returns:
        list: A list of lists, where each sublist represents a point [x, y, z].
    
    Raises:
        FileNotFoundError: If 'input.txt' does not exist.
    """
    try:
        with open("input.txt", "r") as f:
            data = []
            for line in f:
                parts = line.strip().split(',')
                data.append([int(x) for x in parts])
            return data
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Ensure the file is present.")
        raise FileNotFoundError("input.txt missing.")

def squared_dist(a, b):
    """
    Calculates the squared Euclidean distance between points a and b.
    Using squared distance avoids expensive square root operations when 
    only comparison is needed.
    """
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2

def part1():
    """
    Solves Part 1: Finds the product of the sizes of the 3 largest connected 
    components (circuits) formed by the N shortest connections.

    Logic:
    1. Reads the schema points.
    2. Calculates squared Euclidean distances between all unique pairs of points.
    3. Sorts the pairs by distance in ascending order.
    4. Constructs an adjacency list (graph) using only the first N edges 
       (where N is the number of points).
    5. Iterates through the points to find connected components using BFS.
    6. Stores the size of each component found.
    7. Sorts the component sizes descending and returns the product of the top 3.
    """
    points = read_schema()
    n_points = len(points)
    squared_dists = []
    for i, j in combinations(range(n_points), 2):
        dist = squared_dist(points[i], points[j])
        squared_dists.append((dist, (i, j)))
    squared_dists.sort(key=lambda x: x[0])
    adjacency_list = [[] for _ in range(n_points)]
    # Take only as many edges as there are points
    for _, (i, j) in squared_dists[:n_points]:
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)
    visited = [False] * n_points
    component_sizes = []
    for i in range(n_points):
        if visited[i] or not adjacency_list[i]:
            continue
        queue = [i]
        visited[i] = True
        current_size = 0
        while queue:
            node = queue.pop(0)
            current_size += 1
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        component_sizes.append(current_size)
    component_sizes.sort(reverse=True)
    if len(component_sizes) >= 3:
        return component_sizes[0] * component_sizes[1] * component_sizes[2]
    return 0

def check_connectivity(adjacency_list, n_points):
    """
    Checks if the graph is fully connected (i.e., every point is reachable 
    from a starting node).
    
    Logic:
    1. Starts a BFS from node 0.
    2. Counts the number of unique visited nodes.
    3. Returns True if the count equals the total number of points.
    """
    visited = [False] * n_points
    queue = [0] 
    visited[0] = True
    visit_count = 0
    while queue:
        node = queue.pop(0)
        visit_count += 1
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)        
    return visit_count == n_points

def part2():
    """
    Solves Part 2: Determines when the graph becomes fully connected by 
    incrementally adding edges from shortest to longest.

    Logic:
    1. Calculates and sorts all possible edges by distance (ascending).
    2. Initializes an empty graph (adjacency list).
    3. Iterates through the sorted edges, adding them one by one.
    4. After adding an edge, checks if the graph is fully connected.
    5. If fully connected, returns the product of the X coordinates of the 
       two points forming the last added edge.
    """
    points = read_schema()
    n_points = len(points)
    squared_dists = []
    for i, j in combinations(range(n_points), 2):
        dist = squared_dist(points[i], points[j])
        squared_dists.append((dist, (i, j)))
    squared_dists.sort(key=lambda x: x[0])
    adjacency_list = [[] for _ in range(n_points)]
    for _, (i, j) in squared_dists:
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)
        if check_connectivity(adjacency_list, n_points):
            return points[i][0] * points[j][0]
    return 0

if __name__ == "__main__":
    # Solve Part 1
    password_part1 = part1()
    print("--- Part 1: ---")
    print(f"Multiplied together the sizes of the three largest circuits: {password_part1}")
    # Solve Part 2
    password_part2 = part2()
    print("\n--- Part 2: ---")
    print(f"Multiplied together the X coordinates of the last two junction boxes you need to connect: {password_part2}")
