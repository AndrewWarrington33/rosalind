#Given: A string s of length at most 10000 letters.

#Return: The number of occurrences of each word in s, where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.

with open('rosalind_ini6.txt', 'r') as infile:
    lines = infile.readlines()

d = {}

for word in lines.split(' '):
    count = 1
    if word in d:
        d['word'] = count + 1
        count += 1
    else:
        d['word'] = count

