#Import require module
import re

#Read in .txt file
with open('computing_gc_content/rosalind_gc.txt', 'r') as file:
    s = file.read().rstrip()

#Store dna strings in variable dna_strings
dna_strings = re.findall(r'>(Rosalind_\d+)\n([ACGT\n]+)', s)

#Create function to calculate GC% in each dna string
def gc_content(dna):
    G = 0
    C = 0
    length = len(dna.replace('\n', ''))  # Exclude newline characters
    #Add each instance of a G or C to their respective counter
    for letter in dna:
        if letter == "G":
            G += 1
        elif letter == "C":
            C += 1
    #Return percentage of GC content for strand
    return (G + C) / length


max_gc_percent = 0
max_gc_dna = ""
max_gc_header = ""
#Calculate gc % for each sequence
for header, sequence in dna_strings:
    gc_percent = gc_content(sequence)
    #track the sequence with highest gc %
    if gc_percent > max_gc_percent:
        max_gc_percent = gc_percent
        max_gc_dna = sequence
        max_gc_header = header

# Print the DNA string with the highest GC content along with its Rosalind ID
print(f"{max_gc_header}")
print(f"Highest GC content ({max_gc_percent * 100:.6f}%): {max_gc_dna}")



