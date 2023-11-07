# Python Exercises

## Exercise 1

### 1a

print("Hello, World!")

### 1b

my_text = "Hello World!"
print(my_text)


### 1c

print("1", "2", "3", "8")


## Exercise 2

### 2a

glass_of_water = 3

print("I drank", glass_of_water, "glasses of water today.")

### 2b

glass_of_water = 3

glass_of_water = glass_of_water + 1

print(glass_of_water)

## Exercise 3

### 3a

men_stepped_on_the_moon = 12

print(men_stepped_on_the_moon)

### 3b

my_reason_for_coding = "Learn a new skill"

print(my_reason_for_coding)

### 3c

global_mean_sea_level_2018 = 21

global_mean_sea_level_2018 = 21.36

print(global_mean_sea_level_2018)

### 3d

staying_alive = true

print(staying_alive)

## Exercise 4

### 4a

men_stepped_on_the_moon = 12

answer_1 = type(men_stepped_on_the_moon)

print(answer_1)

### 4b

my_reason_for_coding = "Learn a new skill"

answer_2 = type(my_reason_for_coding)

print (answer_2)

### 4c

global_mean_sea_level_delta_2018 = 21.36

answer_3 = type(global_mean_sea_level_delta_2018)

print(answer_3)

### 4d

staying_alive = True

answer_4 = type(staying_alive)

print(answer_4)

### 4e

my_grade = 10

answer_5 = int(my_grade)

print(answer_5)

### 4f

my_temp = 97.70

answer_6 = int(my_temp)

print(answer_6)

### 4g

shoe_price = "69.99"

answer_7 = float(shoe_price)

print(answer_7)

### 4h

gross_world_product = 84.84

gwp_str = str(gross_world_product)

answer_8 = "In 2018 the gross product of the world was " + gwp_str + " trillion US dollars"

print(answer_8)

## Exercise 6

### 6a

lst = [11, 100, 99, 1000, 999]

answer_1 = lst[0]

print(answer_1)

### 6b

lst = [11, 100, 101, 999, 1001]

print(lst[1])

### 6c

lst = [11, 100, 101, 999, 1001]

answer_1 = lst[-1]

print(answer_1)

### 6d

gift_list = ['socks', '4K drone', 'wine', 'jam']

gift_list.append("pajamas")

print(gift_list)

### 6e

gift_list = ['socks', '4K drone', 'wine', 'jam']

gift_list.append(["socks", "tshirt", "pajamas"])

print(gift_list)

### 6f

gift_list = ['socks', '4K drone', 'wine', 'jam']

gift_list.insert(2, "slippers")

print(gift_list)

### 6g

lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]

answer_1 = lst.index(8679)

print(answer_1)

### 6h

lst = ["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]

lst.append(["Navigator", "Suburban"])

print(lst)

### 6i

lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]

lst.remove(99)

print(lst)

### 6j

lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]

lst.reverse()

print(lst)

### 6k

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

answer_1 = lst.count(6)

print(answer_1)

### 6l

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

answer_1 = sum(lst)

print(answer_1)

### 6m

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

answer_1 = min(lst)

print(answer_1)

### 6n

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

answer_1 = max(lst)

print(answer_1)

## Exercise 9

### 9a

str = "It's always darkest before dawn"

print(str)

### 9b

str = "It's always darkest before dawn"

ans_1 = str[0] + str[1] + str[-1]

print(ans_1)

### 9c

str = "It's always darkest before dawn."

str = str.replace(".", "!")

print(str)

### 9d

str = "EVERY Strike Brings Me Closer to the Next Home run."

str = str.lower()

print(str)

### 9e

str = "don't stop me now"

str = str.upper()

print(str)

### 9f

str = "there are no traffic JamS Along The extra mile."

str = str.capitalize()

print(str)

### 9g

str = "There are no traffic jams along the extra mile."

ans_1 = str.startswith("A")

print(ans_1)

### 9h

str = "There are no traffic jams along the extra mile."

ans_1 = str.endswith(".")

print(ans_1)

### 9i

str = "The best revenge is massive success."

ans_1 = str.index("v")

print(ans_1)

### 9j

str = "The best revenge is massive success."

ans_1 = str.find("m")

print(ans_1)

### 9k

str = "The best revenge is massive success."

ans_1 = str.find("X")

print(ans_1)

Comment: .find() returns a -1, .index() returns an Error.

### 9l

str = "People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."

ans_1 = str.count("a")

ans_2 = str.count("o")

print("count of a is: ", ans_1, " count of o is: ", ans_2)

### 9m

v_1 = "1"
v_2 = 1

ans_1 = type(v_1)
ans_2 = type(v_2)

print(ans_1)
print(ans_2)

### 9n

str = "1.975.000"

ans_1 = len(str)

print(ans_1)
