# %%
import re

#Read in .txt file
with open('translating_rna_into_protein/rosalind_prot.txt', 'r') as file:
    s = file.read().rstrip()

#Create mRNA to amino acid dictionary
protein_dict = ({'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V','UUC': 'F', 'CUC': 'L','AUC': 'I', 'GUC': 'V','UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V','UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V','UCU': 'S','CCU': 'P','ACU': 'T','GCU': 'A', 'UCC': 'S' ,'CCC': 'P','ACC': 'T', 'GCC': 'A','UCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A','UCG': 'S','CCG': 'P', 'ACG': 'T','GCG': 'A','UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D','UAC': 'Y', 'CAC': 'H','AAC': 'N','GAC': 'D','UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K','GAA': 'E','UAG': 'Stop',   'CAG': 'Q','AAG': 'K','GAG': 'E','UGU': 'C','CGU': 'R','AGU': 'S', 'GGU': 'G','UGC': 'C','CGC': 'R','AGC': 'S','GGC': 'G','UGA': 'Stop',   'CGA': 'R', 'AGA': 'R', 'GGA': 'G','UGG': 'W', 'CGG': 'R', 'AGG': 'R','GGG': 'G'})

#Translating the mRNA string to amino acid sequence
def translate_mrna_protein(sequence):
    protein_sequence = ''
    if len(sequence) % 3 != 0:
        raise ValueError("mRNA sequence length must be a multiple of 3") #Handle mRNA strings w/ length not a multiple of 3
    
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3] #Define codon as three nucleotides in mRNA
        amino_acid = protein_dict.get(codon, 'Unknown')  # Default to 'Unknown' if the codon is not in the dictionary
        if amino_acid == 'Stop':
            break  # Stop translation if a stop codon is encountered
        protein_sequence += amino_acid
        
    return protein_sequence

# %%
print(translate_mrna_protein(s))

# %%



