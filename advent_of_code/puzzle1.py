numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
values = []

dig_dict = {
    "one": 1, "two": 2, "three": 3, 
    "four": 4, "five": 5, "six": 6, 
    "seven": 7, "eight": 8, "nine": 9, 
    "zero": 0
    }

# Get the input data
text = open("puzzle_1_input", "r")

# Function that reads the numerals and digits 
def read_number(line_text):

    # Go over each character in the line
    for char in range(len(line_text)):
    
        # Check for terms that are one (digits) or three to five (numerals) characters long
        # This corresponds wonderfully to the Rosalind exercises :D
        for length in (1,3,4,5):
            read_str = l_cont[char:char+length]
        # Convert the numerals to digits and add the resulting digits to a list
            if read_str in numbers:
                num_int = str(dig_dict[read_str])
                num_list.append(num_int)
            elif read_str in digits:
                num_list.append(read_str)
    # return the list
    return(num_list)

for l_nr, l_cont in enumerate(text):
    num_list = []
    # execute the function 
    line_digs = read_number(l_cont)
    # concatenate the first and last item of the list and put those in a list
    line_val = line_digs[0] + line_digs[-1]
    values.append(int(line_val))
# sum up
print(sum(values))
text.close()


