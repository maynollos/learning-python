s = "CCAACAAACTGACGTAAACAAACAACAAACTGCGGAACAAACTCAAACAAACAACAAACAACAAACCTTTAACAAACTGCACTAAAACAAACAACAAACACTCTCGCGACATGGAACAAACTAACAAACGGTAACAAACAACCAACAAACGTAACAAACCAACAAACAACAAACCAGAAAACAAACTGAAACAAACAACAAACAACAAACAACAAACAACAAACTATCTCCTAGAGCACTTAAACAAACACAACAAACAAACAAACGGGAACAAACAACAAACAGAACAAACACCAACAAACAACAAACGATCAGCGTTTAACAAACAACAAACCAACAAACTAGGCTTGGCTAACAAACCAATAACAAACAAAGTCAACAAACCCTTATAACAAACAGCGTGGTAACAAACGTAACAAACATTTAACAAACACAACAAACAACAAACCATAACAAACTCAACAAACACTCAACAAACAACAAACCCGCAACAAACAACAAACTTTAACAAACTCAACAAACCCAACAAACTTGAACAAACCTAACAAACGCAACAAACGAACAAACAAAACAAACTAACAAACATCAAAACAAACAACAAACAACAAACGGGAACAAACAGAACAAACAACAAACAACAAACCAACAAACCCGAAACAAACGTTAACAAACAACAAACAACAAACAACAAACATTAACAAACATAACAAACCGTCCTGTCAAACAAACACTGAAACAAACTCCAAACAAACCAACAAACTCACAGAACAAACAACAAACCTGAACAAACTTCGGAACAAACAAGAACAAACTAACAAACTTTAACAAACACAACAAACAACAAACAACAAACCCCGCCGAACAAACCAACAAACCTGACAACAAACCCCCAAAACAAACATAACAAACGGAAACAAACAACAAACAATATGAACAAAC"
t = "AACAAACAA"

# To account for t strings of different lengths
start = 0
stop = len(t)

# go through each t-length segment of s and check if it's the
# same as t, print position if so (answer expects 1-indexed position)
while stop <= len(s):
    if s[start:stop] == t:
        print(start+1, end = " ")
    start += 1
    stop +=1
    

