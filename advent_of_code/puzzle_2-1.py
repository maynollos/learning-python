text = open("puzzle_2_input.txt", "r")
#text = open("puzzle_2_test.txt", "r")
numbers = list(range(1,1000))
numbers = [str(i) for i in numbers]
id_sum = []

# Function seperates numbers and colors and returns both
def count_color(cube_num):
    colors = ["red", "green", "blue"]
    cube_color = ""
    cube_counter = ""
    # Go over each character in the line
    for char in range(len(cube_num)):
        # Check for terms that are one (digits) or three to five (colors) characters long
        for length in (0,1,2,3,4,5):
            read_str = cube_num[char-length:char+1]
    # return every term that matches a number or a color:
            if read_str in numbers:
                cube_counter = int(read_str)
            elif read_str in colors:
                cube_color = read_str
    return(cube_counter, cube_color)
    
# Function checks if the game is possible or not and returns true/false
def check_valid(check_list):
    game_valid = ""
    set_valid = []
    max_count = {
        "red": 12,
        "green": 13,
        "blue": 14
        }
    # go over each set in a game
    for set_nr, set_data in enumerate(check_list):
        color_data = set_data.split(",")
        count_dict = {}
        
        # go over each color in a set with the count_color function
        for color_nr, color in enumerate(color_data):
            color_counts = count_color(color)
            count_dict[color_counts[1]] = color_counts[0]
            
        # check if each color in the set exceeds the maximum
        for color in count_dict:
            if count_dict[color] > max_count[color]:
                set_valid.append("false")
            else:
                set_valid.append("true")
                
    # if a color in the set exceeds the maximum, the game is not valid
    if "false" in set_valid:
        game_valid = "false"
    else:
        game_valid = "true"
    return(game_valid)

# Do the above for each game
for l_nr, l_cont in enumerate(text):
    set_list = []
    
    # parse the strings in the line
    split1 = l_cont.split(":")
    game_id = l_nr + 1
    game_data = split1[1][:-1]
    set_list = game_data.split(";")
    
    # run the check_valid function
    game_bool = check_valid(set_list)
    if game_bool == "true":
        id_sum.append(game_id)

# sum up the ids of every valid game
total = sum(id_sum)
print(total)