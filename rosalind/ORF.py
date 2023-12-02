codontab = {
"UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
"UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
"UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
"UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
"UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
"UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
"UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
"UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
"UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
"UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
"UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
"UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
"UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
"UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
"UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
"UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G" 
	}
	
sequence = ""
fasta = open("rosalind_orf.txt", "r")
output = open("ORF_output.txt", "w")

sclist = []
ulist = []
fw_bw = []
startpos = []
protein_list = []
compdic = {
    "A": "U",
    "C": "G",
    "G": "C",
    "U": "A"
}

# Read input !!Assuming there is only one sequence!!
for line in fasta:
    if line[0] == ">":
        pass
    else:
        sequence += line[:-1]
fasta.close()

# Transcribe
for base in range(len(sequence)):
    if sequence[base] == "T":
        ulist.append("U")
    else:
        ulist.append(sequence[base])
    u = "".join(ulist)
    RNA_fw = u

# Create Reverse Complement
slist = list(RNA_fw)
srevlist = reversed(slist)

for i in srevlist:
    compb = compdic[i]
    sclist.append(compb)

RNA_bw = "".join(sclist)

# Write all reading frames into list
frame1 = RNA_fw
frame2 = RNA_fw[1:]
frame3 = RNA_fw[2:]
frame4 = RNA_bw
frame5 = RNA_bw[1:]
frame6 = RNA_bw[2:]

strands = [frame1, frame2, frame3, frame4, frame5, frame6]

# In each frame
for frame in range(len(strands)):
    startpos = []
    stoppos = []
    prot_range = {}
    codonnr = int(len(strands[frame])/3)
    
    # List off all the start and stop codon positions
    for codon in range(codonnr):
        readcodon = strands[frame][3*codon:3*codon+3]
        if readcodon == "AUG":
            startpos.append(codon)
        elif codontab[readcodon] == "Stop":
            stoppos.append(codon)
    
    # Find the closest subsequent stop to each start codon
    for start in startpos:
        subs_stops = [0]
        for stop in stoppos:
            if stop > start:
                subs_stops.append(stop)
        # Remove the placeholder 0 so it won't be counted as a minimum
        subs_stops.remove(0)
        if subs_stops != []:
            prot_stop = min(subs_stops)
            prot_range[start] = prot_stop
        # If there isn't a subsequent stop codon, mark this sequence so it won't be translated
        else:
            prot_range[start] = "false"
    
    # For each start position
    for proteins in range(len(startpos)):
        protein_seq = ""
        readstart = startpos[proteins]
        # Only read the sequences that have a stop codon
        if prot_range[readstart] != "false":
            readstop = prot_range[readstart]
        read_seq = strands[frame][3*readstart:3*readstop]
        # Translate the sequences
        codonnr = int(len(read_seq)/3)
        for codon in range(codonnr):
            readcodon = read_seq[3*codon:3*codon+3]
            protein_seq += codontab[readcodon]
        if protein_seq not in protein_list:
            protein_list.append(protein_seq)
        # "loading screen" just to have something to look at
        print(".", end="")

# Don't write any empty lines in the output
for protein in protein_list:
    if protein != "":
        output.write(protein)
        output.write("\n")
