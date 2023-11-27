sequences = {}
gccontents = {}
fasta = open("GC_test.fasta", "r")

def gccont(seq): 
    gcon = seq.count("G")
    ccon = seq.count("C")
    gccon = gcon + ccon / len(seq)
    return gccon

for line in fasta:
    if line[0] == ">":
        seqid = line[1:14]
        sequences[seqid] = ""
    else:
        sequences[seqid] += line[:-1]
fasta.close()

for seqid in sequences:
    gccon = gccont(sequences[seqid])
    gccontents[seqid] = gccon

maxgc = max(gccontents, key=gccontents.get)
print("The sequence with the highest GC content is ", maxgc)
    
