#Given: Two positive integers a and b (a<b<10000).

#Return: The sum of all odd integers from a through b, inclusively.

infile = open('conditions_and_loops/rosalind_ini4.txt')

a_and_b = infile.readline()
a_and_b = a_and_b.split(' ')
a = int(a_and_b[0])
b = int(a_and_b[1])

def sum_off_odds(a,b):
    odd_integers = []
    
    if a % 2 == 0:
        a += 1
        odd_integers.append(a)
        while a < b-1:
            a += 2
            odd_integers.append(a)
    
    elif a % 2 != 0:
        odd_integers.append(a)
        while a < b-1:
            a += 2
            odd_integers.append(a)

    if b % 2 != 0:
        odd_integers.append(b)

    return sum(odd_integers)

print(sum_off_odds(a,b))


    