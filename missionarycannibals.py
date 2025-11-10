from collections import deque
def is_valid(state, total_m, total_c):
   m, c, _ = state
   if m > 0 and m < c:
      return False
   dest_m = total_m - m
   dest_c = total_c - c
   if dest_m > 0 and dest_m < dest_c:
      return False
   return True
def solve_missionaries_cannibals(total_m, total_c, boat_cap):
   start_state = (total_m, total_c, 1)
   goal_state = (0, 0, 0)
   queue = deque([(start_state, [])])
   visited = {start_state}
   possible_moves = []
   for m in range(boat_cap + 1):
      for c in range(boat_cap + 1):
         if 0 < m + c <= boat_cap:
            possible_moves.append((m, c))
   while queue:
      current_state, path = queue.popleft()
      if current_state == goal_state:
         return path + [(current_state, "Goal Reached!")]
      m, c, b = current_state
      for dm, dc in possible_moves:
         if b == 1:
            new_m, new_c = m - dm, c - dc
            new_b = 0
            action = f"Send {dm}M, {dc}C"
         else:
            new_m, new_c = m + dm, c + dc
            new_b = 1
            action = f"Bring back {dm}M, {dc}C"
         if 0 <= new_m <= total_m and 0 <= new_c <= total_c:
            next_state = (new_m, new_c, new_b)
            if next_state not in visited and is_valid(next_state, total_m, total_c):
               visited.add(next_state)
               new_path = path + [(current_state, action)]
               queue.append((next_state, new_path))
   return None
def print_solution(solution, total_m, total_c):
   if solution is None:
      print("\nNo solution found for this configuration.")
      return
   print("\n--- Missionaries and Cannibals Solution ---")
   print(f"Step 0: Start -> Left Bank: ({total_m}M, {total_c}C), Right Bank: (0M, 0C), Boat on Left")
   for i, (state_before_move, action) in enumerate(solution):
      m1, c1, b1 = state_before_move
      if i + 1 < len(solution):
         m2, c2, b2 = solution[i+1][0]
      else:
         m2, c2, b2 = state_before_move
      left_bank_after = f"({m2}M, {c2}C)"
      right_bank_after = f"({total_m - m2}M, {total_c - c2}C)"
      boat_pos = "Left" if b2 == 1 else "Right"
      print(f"Step {i+1}: {action} -> Left Bank: {left_bank_after}, Right Bank: {right_bank_after}, Boat on {boat_pos}")
try:
   num_m = int(input("Enter the total number of missionaries: "))
   num_c = int(input("Enter the total number of cannibals: "))
   cap = int(input("Enter the boat capacity: "))
   if num_m < 0 or num_c < 0 or cap <= 0:
      print("Error: Numbers must be non-negative, and boat capacity must be at 3least 1.")
   else:
      solution_path = solve_missionaries_cannibals(num_m, num_c, cap)
      print_solution(solution_path, num_m, num_c)
except ValueError:
   print("Error: Please enter valid integers.") 