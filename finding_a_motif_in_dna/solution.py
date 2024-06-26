#Read in .txt file
with open('finding_a_motif_in_dna/rosalind_subs.txt') as file:
    s, t = file.read().splitlines()  # Split lines to get the two sequences

## Create a function to find the motif in the DNA sequence
def find_motif(s,t):
    length_t = len(t) #Length of the motif sequence
    length_s = len(s) #Length of the DNA sequence
    indices = [] # List to store the starting positions of the motif
     # Loop through the DNA sequence
    for i in range(length_s - length_t + 1):
        # Check if the substring of length 't' starting at position 'i' matches 't'
        if s[i:i+length_t] == t:
            indices.append(i + 1)
            # Append the starting position (1-based index)
    return indices
        
        
# %%
print(find_motif(s,t))


