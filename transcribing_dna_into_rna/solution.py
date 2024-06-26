#Read in .txt file
with open('transcribing_dna_into_rna/rosalind_rna.txt', 'r') as file:
    s = file.read().rstrip()

#Function replacing the T's in DNA with U for RNA
def translate(sequence):
    return sequence.replace('T', 'U')

print(translate(s))