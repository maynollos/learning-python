#strdict = {"AA": "AAATCCC", "BB": "CCCTGGG", "CC": "GGGTAAA"}
sequences = {}
k = 3

fasta = open("rosalind_grph.txt", "r")
#fasta = open("GRPH_test.fasta", "r")
output = open("GRPH_output.txt", "w")

for line in fasta:
    if line[0] == ">":
        seqid = line[1:14]
        sequences[seqid] = ""
    else:
        sequences[seqid] += line[:-1]
fasta.close()

for item in sequences:
    for subitem in sequences:
        if sequences[subitem] != sequences[item] and sequences[subitem][:k] == sequences[item][-k:]:
            print(item, subitem)
            output.write(item + " " + subitem + "\n")