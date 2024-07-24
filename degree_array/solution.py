# In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u
# has, or equivalently, the number of edges incident upon it.

# Given: A simple graph with n ≤ 103 vertices in the edge list format.

# Return: An array D[1..n] where D[i] is the degree of vertex i.

# See Figure 3 for visual example from the sample dataset.

# with open('degree_array/rosalind_deg.txt', 'r') as input:
#     f = input.read()

# arr = []
# for value in f:
#     f.strip()
#     if value.isdigit():
#         arr.append(int(value))

n = 6
m = 7
arr = [1, 2,
       2, 3,
       6, 3,
       5, 6,
       2, 5,
       2, 4,
       4, 1]

d = [0] * n


for i in range(1,n+1):
    for j in range(0,len(arr)):
        if arr[j] == i:
           d[i-1] += 1
print(d)
