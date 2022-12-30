with open('Day 12/Input_12.txt') as f:
  lines = f.read().split('\n')

alphabet = 'SabcdefghijklmnopqrstuvwxyzE'
input = []

said = False

for line in lines:
  temp_line = []
  for char in line:
    temp_line.append(alphabet.index(char))
  input.append(temp_line)

notes_count = 0
for line in input:
  notes_count += len(line)

end_node = 0
start_node = 0
for i in range(len(input)):
  for j in range(len(input[i])):
    if(input[i][j] == 0):
      start_node = i * len(input[i]) + j
    if(input[i][j] == 27):
      end_node = i * len(input[i]) + j

def create_adj_matrix(arr):
  
  
  adj_matrix = [[0 for j in range(notes_count)] for i in range(notes_count)]

  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if(len(arr[i])-1 >= j+1):
        if(0 <= arr[i][j+1] <= arr[i][j] + 1):
          adj_matrix[len(arr[0])*i + j][len(arr[0])*i + j+1] = 1
          adj_matrix[len(arr[0])*i + j+1][len(arr[0])*i + j] = 1
      if(len(arr)-1 >= i+1):
        if(0 <= arr[i+1][j] <= arr[i][j] + 1):
          adj_matrix[len(arr[0])*(i+1) + j][len(arr[0])*i + j] = 1
          adj_matrix[len(arr[0])*i + j][len(arr[0])*(i+1) + j] = 1

  return adj_matrix

adj_matrix = create_adj_matrix(input)




# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			# if(node == end_node):
			print(node, "\t\t", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = 10**100
		global min_index
		
		
		# Search not nearest vertex not in the
		# shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		

		
		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [10**100] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)


# This code is contributed by Divyanshu Mehta


g = Graph(notes_count)
g.graph = adj_matrix



print(start_node)

g.dijkstra(start_node)

print(adj_matrix[2999][3000])
print(input[20][119])

for i in range(len(adj_matrix)):
	if(i == 147):
		for j in range(len(adj_matrix[i])):
			if(adj_matrix[i][j] > 0):
				print(i, j)


# This code is contributed by Divyanshu Mehta and Updated by Pranav Singh Sambyal

