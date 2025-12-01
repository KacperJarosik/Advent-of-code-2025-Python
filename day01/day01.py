# Constants for the Dial Lock
DIAL_SIZE = 100
START_POSITION = 50

def get_rotations():
    """Reads rotations from input.txt or raises an error if not found."""
    try:
        # Reads lines like 'R50', 'L101', etc.
        with open("input.txt", "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Ensure the file is present.")
        raise FileNotFoundError("input.txt missing.")

def part1():
    """
    Solves Part 1: Counts the number of times the dial is left pointing at 0
    after any rotation in the sequence.
    """
    rotations = get_rotations()
    current_position = START_POSITION
    zero_count = 0
    for line in rotations:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            current_position = (current_position + distance) % DIAL_SIZE
        elif direction == 'L':
            current_position = (current_position - distance) % DIAL_SIZE 
        if current_position == 0:
            zero_count += 1
    return zero_count

def part2():
    """
    Solves Part 2: Counts the number of times any click causes the dial to point at 0,
    regardless of whether it happens during a rotation or at the end of one.
    This logic requires counting the passes through 0.
    """
    def calculate_zero_clicks(start_pos, direction, distance):
        """
        Calculates the total number of times the dial hits 0 during the rotation.
        The dial position is 0-99.
        """
        if distance <= 0:
            return 0
        if start_pos == 0:
            return distance // DIAL_SIZE
        if direction == 'L':
            distance_to_first_zero = start_pos
        elif direction == 'R':
            distance_to_first_zero = DIAL_SIZE - start_pos
        if distance < distance_to_first_zero:
            return 0 
        zero_count = 1
        remaining_distance = distance - distance_to_first_zero
        zero_count += remaining_distance // DIAL_SIZE
        return zero_count

    rotations = get_rotations()
    current_position = START_POSITION
    total_zero_count = 0
    for line in rotations:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        total_zero_count += calculate_zero_clicks(current_position, direction, distance)
        if direction == 'R':
            current_position = (current_position + distance) % DIAL_SIZE
        elif direction == 'L':
            current_position = (current_position - distance) % DIAL_SIZE
    return total_zero_count

if __name__ == "__main__":
    # Solve Part 1
    password_part1 = part1()
    print(f"--- Part 1: Final Position Zero Count ---")
    print(f"The password is: {password_part1}")
    # Solve Part 2
    password_part2 = part2()
    print(f"\n--- Part 2: Zero Pass-Through Click Count ---")
    print(f"The password is: {password_part2}")
