# Small program to code Prim's MST algorithm
# Prereqs:
# File "edges.txt" with the format
#
# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

# All edges are undirected with integer edge costs.
# This is a greedy algorithm

# This returns the total cost of the MST

import operator # Used for itemgetter
f = open('edges.txt','r')
a = [line.strip().split() for line in f] # Split each line
f.close()
a = [[int(column) for column in row] for row in a]
num = a.pop(0) # Remove the top row to get the number of rows and edges
nodes = num[0]
edges = num[1]

a.sort(key = operator.itemgetter(2)) # Sort by edge cost
visited = set([]) # Create a visited and unvisited set
not_visited = set([])
for i in range(nodes):
	not_visited.add(i + 1) # Add all nodes to the unvisited set
visited.add(not_visited.pop()) # Start from a single node

total = 0
# For each node and each edge with endpoints i and j
# if i or j is not visited but not both, add the
# unvisited node to visited set and update the total 
# cost.

for j in range(nodes): 
# Since the number of edges may be O(nodes^2), 
# this may limit the runtime
	for i in a:
	# for each edge ordered by cost
		if (i[0] in not_visited and i[1] in visited):
			total += i[2]
			visited.add(i[0])
			not_visited.remove(i[0])
			break
		if (i[1] in not_visited and i[0] in visited):
			total += i[2]
			visited.add(i[1])
			not_visited.remove(i[1])
			break

print total