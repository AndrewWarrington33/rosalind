#Given: Two positive integers a and b (a<b<10000).

#Return: The sum of all odd integers from a through b, inclusively.

def sum_of_odds(a, b):
    odd_integers = []

    # Start from the next odd number if a is even
    if a % 2 == 0:
        a += 1

    # Append all odd numbers from a to b
    for i in range(a, b+1, 2):
        odd_integers.append(i)

    return sum(odd_integers)

# Reading input from file
with open('conditions_and_loops/rosalind_ini4.txt') as infile:
    a_and_b = infile.readline().split()
    a = int(a_and_b[0])
    b = int(a_and_b[1])

print(sum_of_odds(a, b))


    