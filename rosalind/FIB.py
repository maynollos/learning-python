n = 36
k = 3
rp = 1   # rabbit pairs
nr = 0   # new rabbits
nfr = 0   # new fertile rabbits

print("The first ", n, "numbers of the Rabbit sequence are:")
for num in range(n):
    print("Iteration Nr.", num, ":")
    rp = rp + nfr
    print(rp)        # sets the adder to the output from the previous iteration
    nfr = nr         # sets output to sum of adder and memory # prints the output
    nr = rp * k       # sets memory variable to current adder