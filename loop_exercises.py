
# Python loop exercises
	
#	 Exercise 1: Print First 10 natural numbers using while loop
#    Exercise 2: Print the following pattern
#    Exercise 3: Calculate the sum of all numbers from 1 to a given number
#    Exercise 4: Write a program to print multiplication table of a given number
#    Exercise 5: Display numbers from a list using loop
#    Exercise 6: Count the total number of digits in a number
#    Exercise 7: Print the following pattern
#    Exercise 8: Print list in reverse order using a loop
#    Exercise 9: Display numbers from -10 to -1 using for loop
#    Exercise 10: Use else block to display a message “Done” after successful execution of for loop
#    Exercise 11: Write a program to display all prime numbers within a range
#    Exercise 12: Display Fibonacci series up to 10 terms
#    Exercise 13: Find the factorial of a given number
#    Exercise 14: Reverse a given integer number
#    Exercise 15: Use a loop to display elements from a given list present at odd index positions
#    Exercise 16: Calculate the cube of all numbers from 1 to a given number
#    Exercise 17: Find the sum of the series upto n terms
#    Exercise 18: Print the following pattern

# Nr.1

for i in range(1,11):
   print(i)

# Prints each range index on a range from 1 to 10.


## Nr.2 ##

numlist = []

for i in range(1,6):
    numlist.append(i)
    print(numlist)

# Appends the range index to the list each iteration and prints the list.
# After looking at the solution, I realised this is not actually what the exercise
# called for so I wrote this:

rows = 5

for i in range(1, rows + 1):
    for j in range(1,i + 1):
        print(j, end = " ")
    print()
    
# which is basically just the solution, but I can't seem to figure out why an
# empty print function creates a line break at that point

# Nr.3

a = 1           # variables we want to add integers between
b = 100
result = []     # list for summing up the result

for n in range(a, b+1):     # b + 1 because 
    if n % 2 == 1:          # modulo is not required in this case because we want all the integers, not just the odd ones
        result.append(n)    # put all the integers in a list
print(sum(result))          # print the sum of the list

#Reviewed the Rosalind INI4 example^^


## Nr.4 ##

factor = 3                 # number we want multiplied

for i in range(1,11):      # create range from 1 to 10 to multiply with
    product = i * factor   # multiply range index with factor
    print(product)         # print result
    
    
## Nr.5 Display numbers from a list using loop ##

 numbers = [12, 75, 150, 180, 145, 525, 50]       # List to print numbers from

for i in range(len(numbers)):
#    first check if numbers is larger than 500
#    this has to come first or else the script will continue instead of breaking
    if numbers[i] > 500:    
        break
#    then check if the number is not divisible by 5 or greater than 150
    elif numbers[i]%5 != 0 or numbers[i] > 150:
        continue
#    print it if it checks all the boxes
    else:
        print(numbers[i])


## Nr.6 Count the total number of digits in a number ##

# I get that the exercise calls for a while loop but wouldn't it be much more
# straightforward to do it like this:

num = 123456789
#first convert the number to a string so it can be itrated
numstr = str(num)
#create a list with the digits of the number
diglist = list(numstr)
#print the length of the list
print(len(diglist))


## Nr.7 Print a reverse number pattern ##

#Define where we want the pattern to start and fill a
#list with a range from 1 to a
a = 5
starter = [*range(1,a+1)]
while starter != []:
#repeat until the list is empty, printing a page break and
#removing one item from the list each time:
    for i in range(1, len(starter)+1):
        print(starter[-i], end = " ")
        #print the list backwards each iteration
    print()
    starter.pop()
    # remove one list item
    
# It's uglier than the solution but it's my ugly little coding baby and I'm
# proud of it the way it is


## Nr.8 Print list in reverse order using a loop ##

list1 = [10, 20, 30, 40, 50]

for i in range(1, len(list1) + 1):
    print(list1[-i])
    # just print the list with the index reversed
    
# If it works it aint stupid I guess but the solution is easier


## Nr.10 Use else block to display a message “Done” after successful execution of for loop ##

for i in range(5):
    print(i)
else:
    print("Done!")  # In a for loop, the else block executes when the for loop is finished.
    
    
## Nr.11 Write a program to display all prime numbers within a range ##

start = 25
end = 50

for i in range(start, end + 1):
    if i > 1:
        for fac in range(2, i):
            if (i % fac) == 0:
                break
        else:
            print(i)

# Essentially just worked through the solution step by step because I couldn't
# figure it out myself (I wasn't expecting the solution to just be brute force)


## Nr.12: Display Fibonacci series up to 10 terms ##

end = 15
out = 0   # output variable
mem = 1   # memory variable
add = 0   # adder variable

print("The first ", end, "numbers of the Fibonacci sequence are:")
for num in range(end-1):
    add = out           # sets the adder to the output from the previous iteration
    out = mem + add     # sets output to sum of adder and memory
    print(out, end=" ") # prints the output
    mem = add           # sets memory variable to current adder
    
# The memory needs to be 1 in the beginning because else two 0s would be added
# which would not iterate.


## Nr.13: Find the factorial of a given number ##

num = 8
result = 1

for i in range(1, num + 1):
    result = result * i
print(result)

# Didn't think of specifying what to do in the edge cases covered in the solution
# but the core idea is the same


## Nr.14: Reverse a given integer number ##

# Now I know why Nr.6 works better with loops.


## Nr.15: Use a loop to display elements from a given list present at odd index positions ##

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if i % 2 != 0:
        print(my_list[i])

# Essentially what we did with Rosa INI4.


## Nr.16: Calculate the cube of all numbers from 1 to a given number ##

num = 6

for i in range(1, num+1):
    squ = i**3
    print("Current number is", i, "and its cube is", squ)
    
# Also quite straightforward considering what we did in class


## Nr.17: Find the sum of the series upto n terms ##

n = 5
x = "2"
sumlist = []
result = 0

for i in range(1,n+1):
    sumlist.append(x*i)
    #appends the terms of the series to the list
    result += int(sumlist[i-1])
    #adds the terms together
print(result)
    
# I feel like this works kind of like the solution online but I don't understand
# the solution and mine seems fine as well


## Nr.18 ##

mx = 5

#print more asterisks per iteration up to the defined maximum:
for i in range(1, mx+1):
    print("* " * i)

#print fewer asterisks per iteration after the defined maximum:
for i in range(mx-1,0,-1):
    print("* " * i)

# This actually seems simpler than the solution, what am I missing?

