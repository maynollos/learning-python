## INI1:

The command "import this" given by the assignment returned a poem
or mantra of sorts that I assume has some kind of spiritual meaning
to python programmers ;)

## INI2:

Application of the pythagorean theorem, the download provided random
numbers between 1 and 1000. I solved it by using the up key to retrieve
the pythagorean theorem code we wrote in class yesterday:

c = (a**2 + b**2)**0.5

print (c)

The problem called for the square of the hypotenuse, so I removed the
square root:

c = (a**2 + b**2)

print (c)

And finally, I assigned the given values to the corresponding variables:

a = 892
b = 891

c = (a**2 + b**2)

print (c)

which yielded the (correct) answer, 1589545.

## INI3:

Slicing a string of jumbled characters according to given values. I wrote
the following:

str = "oOL6O5FkCM0ziie9SIDsBnSw0QUrwomMuJfY0cCnq2saxLNGotTSyrrhaptesv2upctXCDxwqvRyfUIJXvcqgyNBuuyeNRDIcl362D5zty1EkkshpunJXKG3h24pMoSw6vZ3wkG81SK8qzIrqLNOcnPPKSokarelinikLBLph."

word1 = str[51:61]
word2 = str[155:163]
print word1 + " " + word2

which of course returned a Syntax Error because I had forgotten the
parentheses that print() requires, and after adding those, the code
provided two words:

str = "oOL6O5FkCM0ziie9SIDsBnSw0QUrwomMuJfY0cCnq2saxLNGotTSyrrhaptesv2upctXCDxwqvRyfUIJXvcqgyNBuuyeNRDIcl362D5zty1EkkshpunJXKG3h24pMoSw6vZ3wkG81SK8qzIrqLNOcnPPKSokarelinikLBLph."

word1 = str[51:61]
word2 = str[155:163]
print(word1 + " " + word2)

Syrrhaptes karelini

(which must be a very strange animal since Syrrhaptes is a genus of
grouse and karelini is the epithet of a snake species from the family 
Colubridae)


