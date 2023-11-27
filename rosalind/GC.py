# Two dicitonaries with the sequence IDs, one with the raw
# sequences and one with the GC content of each sequence
sequences = {}
gccontents = {}

# Open the input file
fasta = open("rosalind_gc.txt", "r")
#fasta = open("gc_test.fasta", "r")
output = open("GC_output.txt", "w")

# function that calculates the GC content
def gccont(seq): 
    gcon = seq.count("G")
    ccon = seq.count("C")
    gccon = ((gcon + ccon) / len(seq))*100
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

# find the ID of the maximum GC content and print it, also
# write an output file for uploading to rosalind
maxgcID = max(gccontents, key=gccontents.get)
maxgc = max(gccontents.values())
output.write(str(maxgcID))
output.write("\n")
output.write(str(maxgc))
print("The sequence with the highest GC content is ", maxgcID)
print("The GC content of this sequence is ", maxgc)
    
