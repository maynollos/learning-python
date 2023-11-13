#shopping = ["bread", "potatoes", "eggs", "flour", "rubber duck", "pizza", "milk"]
#new_items = ["cheese", "flour", "eggs", "spaghetti", "sausages", "bread"]
#for item in new_items:
#    shopping.append(item)
#print(shopping)

shopping = ['bread', 'potatoes', 'eggs', 'flour', 'rubber duck', 'pizza', 'milk']
amounts =  ['1',     '10',       '12',    '1',    '2',            '5',     '1']
prices = [3, 0.5, 1.2, 5.3, 13.7, 16, 1.47]
sumprice =[]

for i in range(len(shopping)):
    s = 'I need to buy ' + amounts[i] + ' ' + shopping[i]
    print(s)
   
for i in range(len(shopping)):
    itemprice = int(amounts[i]) * prices[i]
    sumprice.append(itemprice)

p = str(sum(sumprice))
t = "\nIt will cost me " + p + "€ in total"
print(t)