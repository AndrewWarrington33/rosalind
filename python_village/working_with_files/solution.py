#Given: a file containing at most 1000 lines.

#Return: A file containing all the even-numbered lines from the original file. 
#Assume 1-based numbering of lines.

#Reading input from .txt file

with open('rosalind_ini5.txt', 'r') as infile:
    lines = infile.readlines()

output = open('output.txt', 'w')

for i in range(1,len(lines),2):
    output.write(lines[i])

output.close()