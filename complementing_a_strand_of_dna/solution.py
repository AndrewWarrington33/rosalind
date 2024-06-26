#Read in .txt file
with open('complementing_a_strand_of_dna/rosalind_revc.txt', 'r') as file:
    s = file.read().rstrip()
    #Creating a dictionary with each nucleotides respective complement
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
#Making the reverse complement of the dna sequence
reverse_complement = "".join(complement.get(base, base) for base in reversed(s))
print(reverse_complement)