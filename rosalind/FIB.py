n = 36
k = 3
rp = 1   # rabbit pairs
nr = 0   # new rabbits
nfr = 0   # new fertile rabbits

print("The first ", n, "numbers of the Rabbit sequence are:")
for num in range(n):
    print("Iteration Nr.", num, ":")
    rp = rp + nfr    # add new fertile rabbits to previous number of rabbits
    print(rp)        # print current number of rabbits
    nfr = nr         # previous new rabbits are now fertile
    nr = rp * k      # new rabbits are three times current rabbits