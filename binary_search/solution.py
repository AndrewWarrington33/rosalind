def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid + 1  # Return 1-based index

    return -1

# Read input from file
with open('binary_search/rosalind_bins.txt', 'r') as input_file:
    values = input_file.readlines()

# Parse the input data
n = int(values[0].strip())
m = int(values[1].strip())
a = list(map(int, values[2].strip().split()))
lis = list(map(int, values[3].strip().split()))

# Initialize output list
output = []

# Perform binary search for each element in lis
for value in lis:
    result = binary_search(a, value)
    output.append(result)

# Write the output to a .txt file
with open('binary_search/output.txt', 'w') as file:
    # Write each item in output separated by a space
    file.write(" ".join(map(str, output)) + "\n")

# Print the output for verification
print(output)
