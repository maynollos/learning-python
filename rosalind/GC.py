sequences = {}
seqgc = {}
fasta = open("GC_test.fasta", "r")

def gccontent(seq): 
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
    gccon = gccontent(sequences[seqid])
    seqgc[seqid] = gccon

maxgc = max(seqgc, key=seqgc.get)
print("The sequence with the highest GC content is ", maxgc)
    
