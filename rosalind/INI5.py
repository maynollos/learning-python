
text = open("rosalind_ini5.txt", "r")
output = open("ini5_output.txt", "a")

for lnr, lcont in enumerate(text):
    if lnr%2 == 1:
        # print(lnr, lcont)
        output.write(lcont)
    
text.close()