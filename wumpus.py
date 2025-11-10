import random

def create_world(grid_size=4):
   player_position = (0, 0)
   available_squares = [(row, col) for row in range(grid_size) for col in range(grid_size)]
   available_squares.remove(player_position)
   wumpus_location, gold_location, *pit_locations = random.sample(
      available_squares, k=random.randint(3, grid_size + 2)
   )
   return {
      "player_pos": player_position,
      "wumpus_loc": wumpus_location,
      "gold_loc": gold_location,
      "pit_locs": pit_locations,
      "grid_size": grid_size,
   }

def display_grid(game_state, reveal_all=False):
   size = game_state["grid_size"]
   print("-" * (size * 2 + 1))
   for row in range(size - 1, -1, -1):
      row_display = []
      for column in range(size):
         current_pos = (row, column)
         if current_pos == game_state["player_pos"]:
            row_display.append("A")
         elif reveal_all and current_pos == game_state["wumpus_loc"]:
            row_display.append("W")
         elif reveal_all and current_pos == game_state["gold_loc"]:
            row_display.append("G")
         elif reveal_all and current_pos in game_state["pit_locs"]:
            row_display.append("P")
         else:
            row_display.append("?" if not reveal_all else ".")
      print("|" + "|".join(row_display) + "|")
   print("-" * (size * 2 + 1))

def update_player_position(game_state, direction):
   row, column = game_state["player_pos"]
   size = game_state["grid_size"]
   if direction == "up" and row + 1 < size:
      row += 1
   if direction == "down" and row - 1 >= 0:
      row -= 1
   if direction == "left" and column - 1 >= 0:
      column -= 1
   if direction == "right" and column + 1 < size:
      column += 1

   game_state["player_pos"] = (row, column)
   if game_state["player_pos"] == game_state["wumpus_loc"]:
      return "You were eaten by the Wumpus! 💀"
   if game_state["player_pos"] in game_state["pit_locs"]:
      return "You fell into a bottomless pit! 😱"
   if game_state["player_pos"] == game_state["gold_loc"]:
      return "You found the shimmering gold! 💰 You win!"

   return None

if __name__ == "__main__":
   current_game = create_world()
   print("Welcome to Wumpus World! Your goal is to find the gold (G).")
   print("Moves: up, down, left, right")
   display_grid(current_game)
   while True:
      move_command = input("Your move: ").strip().lower()
      game_result = update_player_position(current_game, move_command)

      display_grid(current_game)
      if game_result:
         print(f"\n--- GAME OVER ---\n{game_result}\n")
         print("Revealing the map:")
         display_grid(current_game, reveal_all=True)
         break