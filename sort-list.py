fruits = ["apple", "mango", "kiwi", "banana", "pear", "grapes"]   

fruits.sort()

print(fruits)

numList = [55, 45, 23, 87, 1]
numList.sort()

print(numList)

print("\n")

fruits.sort(reverse = True)
print(fruits)

numList.sort(reverse = True)
print(numList)


# Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n-50)
    
newList = [100, 50, 82, 23, 65]
newList.sort(key =myfunc)
print(newList)


#case sensitive

fruitBasket = ["banana", "Mango", "Orange", "apple"]
fruitBasket.sort()
print(fruitBasket)


fruitBasket.sort(key = str.lower)
print(fruitBasket)

print("\n")

myFruitBasket = ["banana", "Mango", "Orange", "apple"]
myFruitBasket.reverse()
print(myFruitBasket)
