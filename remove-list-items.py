# remove list items

kitchenitems = ["Stove", "Plate", "Cooker", "Spoon"]

kitchenitems.remove("Stove")

print(kitchenitems)

#If there are more than one item with the specified value, the remove() 
#method removes the first occurrence:

kitchenitems = ["Stove", "Plate", "Cooker", "Spoon", "Plate"]

kitchenitems.remove("Plate")
print(kitchenitems)


dinnerset = ["Plate", "Bowl", "Spoon", "Fork"]

dinnerset.pop(1)
print(dinnerset)


dinnerset = ["Plate", "Bowl", "Spoon", "Fork"]

del dinnerset[0]
print(dinnerset)

a = ["Plate", "Bowl", "Spoon", "Fork"]

del a

g = ["Plate", "Bowl", "Spoon", "Fork"]

g.clear()
print(g)



