fruits = ["apple", "mango", "cherry", "banana", "kiwi", "pear"]
newlist = []

for x in fruits:
    if "e" in x:
        newlist.append(x)
    
print(newlist)    


fruits = ["apple", "mango", "cherry", "banana", "kiwi", "pear"]

newlist = [i for i in fruits if "e" in i]    
print(newlist)    

numlist = [i for i in range(11)]
print(numlist)

fruits = ["apple", "mango", "cherry", "banana", "kiwi", "pear"]


newlist = [i for i in fruits if "e" in i]
    

print(newlist)    

numlist = [i for i in range(11)]
print(numlist)

numlist = [i for i in range(10) if i < 5]
print(numlist)

newfruitslis = [f.upper() for f in fruits]
print(newfruitslis)

print("\n")

#"Return the item if it is not banana, if it is banana return orange".

againNewList = [x if x != "banana" else "orange" for x in fruits]
print(againNewList)
