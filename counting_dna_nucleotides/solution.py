#Read in .txt file
with open('counting_dna_nucleotides/rosalind_dna.txt', 'r') as file:
    s = file.read().rstrip()
   
#Function to count each dna nucleotide 
    def nucleotide_count(sequence):
        #initialize counts at 0
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        #loop over dna sequence
        for nt in sequence:
            #add to nucleotide count
            if nt == "A":
                a_count += 1
            if nt == "C":
                c_count += 1
            if nt == "G":
                g_count += 1
            if nt  == "T":
                t_count += 1
        print (a_count, c_count, g_count, t_count)
nucleotide_count(s)