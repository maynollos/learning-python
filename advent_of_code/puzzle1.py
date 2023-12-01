numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
values = []

digdict = {
    "one": 1, "two": 2, "three": 3, 
    "four": 4, "five": 5, "six": 6, 
    "seven": 7, "eight": 8, "nine": 9, 
    "zero": 0
    }

# Get the input data
text = open("puzzle_1_input", "r")

# Function that reads the numerals and digits 
def readnumber():

    # Go over each character in the line
    for char in range(len(lcont)):
    
        # Check for terms that are one (digits) or three to five (numerals) characters long
        # This corresponds wonderfully to the Rosalind exercises :D
        for length in (1,3,4,5):
            readstr = lcont[char:char+length]
        # Convert the numerals to digits and add the resulting digits to a list
            if readstr in numbers:
                numint = str(digdict[readstr])
                numlist.append(numint)
            elif readstr in digits:
                numlist.append(readstr)
    # return the list
    return(numlist)

for lnr, lcont in enumerate(text):
    numlist = []
    # execute the function 
    linedigs = readnumber()
    # concatenate the first and last item of the list and put those in a list
    lineval = linedigs[0] + linedigs[-1]
    values.append(int(lineval))
# sum up
print(sum(values))
text.close()


