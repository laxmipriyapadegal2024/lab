from collections import deque
import math
def solve(j1_cap, j2_cap, target):
    path_map = {}
    visited = set()
    queue = deque()
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    path_map[start] = (None, "Initial State")
    while queue:
        j1, j2 = queue.popleft()
        state = (j1, j2)
        if j1 == target or j2 == target:
            path = []
            curr = state
            while curr is not None:
                parent, action = path_map.get(curr)
                path.append((curr, action))
                curr = parent
            return path[::-1]
        moves = []
        moves.append(((j1_cap, j2), "Fill Jug 1"))
        moves.append(((j1, j2_cap), "Fill Jug 2"))
        moves.append(((0, j2), "Empty Jug 1"))
        moves.append(((j1, 0), "Empty Jug 2"))
        pour12 = min(j1, j2_cap - j2)
        moves.append(((j1 - pour12, j2 + pour12), "Pour from Jug 1 to Jug 2"))
        pour21 = min(j2, j1_cap - j1)
        moves.append(((j1 + pour21, j2 - pour21), "Pour from Jug 2 to Jug 1"))
        for next_s, action in moves:
            if next_s not in visited:
                visited.add(next_s)
                path_map[next_s] = (state, action)
                queue.append(next_s)
    return None
jug1_cap = int(input("Enter the capacity of the first jug: "))
jug2_cap = int(input("Enter the capacity of the second jug: "))
target_amount = int(input("Enter the target amount to measure: "))
if jug1_cap <= 0 or jug2_cap <= 0 or target_amount < 0:
    print("\nError: Capacities must be positive integers, and the target cannot be negative.")
elif target_amount % math.gcd(jug1_cap, jug2_cap) != 0:
        print("\nNo solution possible.")
        print(f"The target amount ({target_amount}) must be a multiple of the greatest common divisor of the jug capacities ({math.gcd(jug1_cap, jug2_cap)}).")
else:
    print(f"\nSolving for J1={jug1_cap}, J2={jug2_cap}, Target={target_amount}\n")
    solution = solve(jug1_cap, jug2_cap, target_amount)
    if solution:
        print("Solution found! Here is the path:")
        for i, (state, action) in enumerate(solution):
            print(f"Step {i}: State ({state[0]:>2}, {state[1]:>2}) - {action}")
    else:
        print("No solution found. The target amount might be larger than both jugs.")