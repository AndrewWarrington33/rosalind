# Read the input file
with open('dictionaries/rosalind_ini6.txt', 'r') as infile:
    content = infile.read().strip()  # Read and strip any leading/trailing whitespace

# Split the content into words
words = content.split()

# Initialize a dictionary to count occurrences
word_count = {}

# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Write the output file
with open("dictionaries/output.txt", "w") as output:
    for word, count in word_count.items():
        output.write(f"{word} {count}\n")