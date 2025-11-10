import itertools
def travelling_salesman(distance_matrix, start=0):
   n = len(distance_matrix)
   cities = list(range(n))
   cities.remove(start)
   min_path = None
   min_cost = float('inf')
   for perm in itertools.permutations(cities):
      current_cost = 0
      k = start
      for j in perm:
         current_cost += distance_matrix[k][j]
         k = j
      current_cost += distance_matrix[k][start]
      if current_cost < min_cost:
         min_cost = current_cost
         min_path = (start,) + perm + (start,)
   return min_path, min_cost
distance_matrix = [
[0, 29, 20, 21],
[29, 0, 15, 17],
[20, 15, 0, 28],
[21, 17, 28, 0]
]
path, cost = travelling_salesman(distance_matrix)
print("Optimal path:", path)
print("Minimum cost:", cost)