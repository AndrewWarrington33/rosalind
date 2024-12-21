import pandas as pd
import numpy as np
import re

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

# Return: The adjacency list corresponding to O3. 
# You may return edges in any order.

# Read in .txt file
with open('overlap_graphs/rosalind_grph.txt', 'r') as file:
    file_content = file.read().rstrip()

# Use regex to find all dna sequences and their identifiers
dna_sequences = re.findall(r'>(Rosalind_\d+)\n([ACGT\n]+)', file_content)

# Replace new line characters with empty strings
dna_sequences = [(identifier, sequence.replace('\n', '')) for identifier, sequence in dna_sequences]

# Convert list of tuples into pandas dataframe
dna_df = pd.DataFrame(dna_sequences)

# Extract dna sequences from dataframe
sequences = dna_df[1]

# Create matrix where each row represents a dna sequence
sequence_matrix = []
for i in sequences:
    sequence_matrix.append([j for j in i])
M = np.array(sequence_matrix, dtype=object)

def overlap(matrix):
    # Initialize an empty list to store the adjacency list
    adjacency_list = []
    # Loop through each pair of sequences
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # Skip the comparison if the sequences are the same
            if i == j:
                continue
            # Check if the last three characters of the first sequence match the first three characters of the second sequence
            if matrix[i][-3:] == matrix[j][:3]:
                # Append the identifiers of the sequences to the adjacency list
                adjacency_list.append((dna_df.iloc[i, 0], dna_df.iloc[j, 0]))
    return adjacency_list

adjacency_list = overlap(sequence_matrix)

# Save the adjacency list to a .txt file
with open('overlap_graphs/adjacency_list.txt', 'w') as file:
    for edge in adjacency_list:
        file.write(f"{edge[0]} {edge[1]}\n")

