sequences = {}
fasta = open("GC_test.fasta", "r")

def gccontent(): 
    print(seqid.count(G))

for line in fasta:
    if line[0] == ">":
        seqid = line[1:14]
        sequences[seqid] = ""
    else:
        sequences[seqid] += line[:-1]
fasta.close()

for seqid in sequences:
    gccontent()
