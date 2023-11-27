# Two dicitonaries with the sequence IDs, one with the raw
# sequences and one with the GC content of each sequence
sequences = {}
gccontents = {}

# Open the input file
fasta = open("GC_test.fasta", "r")

# function that calculates the GC content
def gccont(seq): 
    gcon = seq.count("G")
    ccon = seq.count("C")
    gccon = gcon + ccon / len(seq)
    return gccon

# Parsing the fasta file, put IDs and their corresponding
# sequences into the sequences dictionary
for line in fasta:
    if line[0] == ">":
        seqid = line[1:14]
        sequences[seqid] = ""
    else:
        sequences[seqid] += line[:-1]
fasta.close()

# put each GC content into the gccontents dictionary
for seqid in sequences:
    gccon = gccont(sequences[seqid])
    gccontents[seqid] = gccon

# find the ID of the maximum GC content and print it
maxgc = max(gccontents, key=gccontents.get)
print("The sequence with the highest GC content is ", maxgc)
    
