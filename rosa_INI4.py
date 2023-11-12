#Given: Two positive integers a and b (a < b < 10000).
#Return: The sum of all odd integers from a through b, inclusively

a = 10
b = 100
result = 0
#adder = 0

#while adder <= b-1 :
#   result = result + (a + adder)
#   adder = adder + 1
#   print("result currently is", result)
#   print("adder currently is", adder)
  
#print(result)

# Above is how I tried to solve this before coming back to the group solution,
# it works (I think) if a is 1 but not otherwise and fixing that problem would
# just not be worth it considering that this is already more complicated than the
# solution below

for n in range(a, b+1):
    if n % 2 == 1:
        result.append(n)
print(sum(result))

