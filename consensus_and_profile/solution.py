#Load required packages
import numpy as np
import re
import pandas as pd

#Read in .txt file
with open('consensus_and_profile/rosalind_cons.txt', 'r') as file:
    s = file.read().rstrip()

#Use regex to find all dna sequences and their identifiers
dna = re.findall(r'>(Rosalind_\d+)\n([ACGT\n]+)', s)


#Replace new line characters with empty strings
dna = [(identifier, sequence.replace('\n', '')) for identifier, sequence in dna]


#Convert list of tuples into pandas dataframe
dna_dataframe = pd.DataFrame(dna)

#Extract dna sequences from dataframe
dna_strings = dna_dataframe[1]

#Create matrix where each row represents a dna sequence
final_matrix = []
for i in dna_strings:
    final_matrix.append([j for j in i])
M = np.array(final_matrix).reshape(len(final_matrix),len(final_matrix[0]))


# %%
def profile_consensus(matrix):
    # Initialize lists to store counts of each nucleotide
    A = []
    C = []
    G = []
    T = []
    # Loop through each column of the matrix
    for i in range(len(matrix[0])):
        # Initialize counts for each nucleotide in the current column
        A_count = 0
        C_count = 0
        G_count = 0
        T_count = 0
        # Count the occurrences of each nucleotide in the current column
        for j in M[:,i]:
            if j == "A":
                A_count += 1
            elif j == "C":
                C_count += 1
            elif j == "G":
                G_count += 1
            elif j == "T":
                T_count += 1
        # Append the counts to the respective lists
        A.append(A_count)
        C.append(C_count)
        G.append(G_count)
        T.append(T_count)
    # Create a dictionary for the profile matrix
    profile_matrix = {"A": A, "C": C, "G": G, "T": T}
    # Print the profile matrix
    for k, v in profile_matrix.items():
        print(k + ": " + " ".join(str(x) for x in v))

    # Create a consensus string
    P = []
    P.append(A)
    P.append(C)
    P.append(G)
    P.append(T)
    profile = np.array(P).reshape(4, len(A))
    consensus = []
    for i in range(len(A)):
        # Determine the consensus nucleotide for each position
        if max(profile[:,i]) == profile[0,i]:
            consensus.append("A")
        elif max(profile[:,i]) == profile[1,i]:
            consensus.append("C")
        elif max(profile[:,i]) == profile[2,i]:
            consensus.append("G")
        elif max(profile[:,i]) == profile[3,i]:
            consensus.append("T")
    #Print the consensus string
    print("".join(consensus))

# %%
profile_consensus(final_matrix)

