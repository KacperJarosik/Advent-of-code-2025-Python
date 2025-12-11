import re
from itertools import product
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def read_data(filename="input.txt"):
    """
    Reads the machine input file.
    
    Returns a list of tuples:
    - target states (list of 0/1) for Part 1
    - button indices (list of lists) for Part 1
    - button indices (list of lists) and jolts (list of ints) for Part 2
    """
    part1_data = []
    part2_data = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # --- Part 1 parsing ---
            # Indicator lights inside square brackets
            diagram = line.split("[")[1].split("]")[0].strip()
            target = [1 if c == "#" else 0 for c in diagram]
            # Button lists inside parentheses
            parts = line.split("(")[1:]
            buttons = []
            for p in parts:
                inside = p.split(")")[0]
                if inside.strip():
                    nums = [int(x) for x in inside.split(",") if x.isdigit()]
                    buttons.append(nums)
            part1_data.append((target, buttons))
            
            # --- Part 2 parsing ---
            button_strs = re.findall(r"\(([^)]*)\)", line)
            buttons2 = []
            for button in button_strs:
                inds = [int(x) for x in button.split(",")]
                buttons2.append(inds)
            m = re.search(r"\{([^}]*)\}", line)
            jolts = [int(x) for x in m.group(1).split(",")] if m else []
            part2_data.append((buttons2, jolts))
    return part1_data, part2_data


def part1(data):
    """
    Computes the minimum number of presses needed to reach the target lights
    for all machines using brute-force search.
    """
    def presses_needed(target, buttons):
        n = len(buttons)
        L = len(target)
        best = None
        for choice in product([0, 1], repeat=n):
            state = [0] * L
            for btn_index, pressed in enumerate(choice):
                if pressed:
                    for lamp in buttons[btn_index]:
                        state[lamp] ^= 1  # toggle
            if state == target:
                presses = sum(choice)
                if best is None or presses < best:
                    best = presses
        return best
    total = 0
    for target, buttons in data:
        total += presses_needed(target, buttons)
    return total


def part2(data):
    """
    Computes the minimum total presses using Integer Linear Programming (ILP)
    to exactly match the jolts for each machine.
    """
    total = 0
    for buttons, jolts in data:
        n = len(jolts)
        m = len(buttons)
        A = np.zeros((n, m), dtype=int)
        for j, inds in enumerate(buttons):
            for i in inds:
                A[i, j] = 1
        c = np.ones(m, dtype=float)
        jolts_array = np.array(jolts, dtype=float)
        lc = LinearConstraint(A, lb=jolts_array, ub=jolts_array)
        bounds = Bounds(lb=np.zeros(m), ub=np.full(m, np.inf))
        integrality = np.ones(m, dtype=int)
        res = milp(c=c, constraints=[lc], bounds=bounds, integrality=integrality)
        if res.status != 0:
            raise RuntimeError(f"ILP failed with status {res.status}: {res.message}")
        total += int(round(res.fun))
    return total


if __name__ == "__main__":
    part1_data, part2_data = read_data("input.txt")
    # Solve Part 1
    result1 = part1(part1_data)
    print("--- Part 1: ---")
    print(f"The largest area of any rectangle you can make: {result1}")
    # Solve Part 2
    result2 = part2(part2_data)
    print("\n--- Part 2: ---")
    print(f"The largest area of any rectangle you can make using only red and green tiles: {result2}")
