# In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u
# has, or equivalently, the number of edges incident upon it.

# Given: A simple graph with n ≤ 103 vertices in the edge list format.

# Return: An array D[1..n] where D[i] is the degree of vertex i.

# See Figure 3 for visual example from the sample dataset.

with open('degree_array/rosalind_deg.txt', 'r') as input:
    f = input.read()

elements = f.split()
arr = [int(element) for element in elements]

n = arr[0]  # number of vertices
m = arr[1]  # number of edges

# Initialize the degree array with zeros
d = [0] * n

# Read the edges and update the degree array
for i in range(2, len(arr), 2):
    u = arr[i]
    v = arr[i+1]
    d[u-1] += 1
    d[v-1] += 1

with open('degree_array/output.txt', 'w') as file:
    # Write each item in output separated by a space
    file.write(" ".join(map(str, d)) + "\n")

print(d)