letters = ["a", "b", "c"]
matrix = [[0,1], [2,3]]
numbers = list(range(20))

chars = list("Hello World")
print (chars)



'Accessing items'

letters [0] = "A"
print(numbers[0:3])
print(numbers[::-2])

'Unpacking list'
mynumbers = [1,2,3,4,5,6]
first, second, *other ,last = mynumbers
print (first)
print (other)
print (last)


'Looping over a list'
for index , letter in enumerate(letters):
    print(index , letter)
'Adding or Removing Item'

# Add
letters.append("d")
letters.insert(0,"-")
print(letters)

# Remove
letters.pop()
print(letters)
letters.remove("b")
print (letters)

del letters[0:3]
print(letters)
letters.clear()
print(letters)


'Finding Item'
myletters = ["a","b","c"]
if "b" in myletters:
    print(myletters.index("b"))

'Sorting List'
numbers.sort(reverse=True)

'Lambda Function => One line anonymous function that you can pass to other functions'
items = [("Product1",10),("Product2",9),("Product3",12)]
items.sort(key=lambda item:item[1])
print(items)


'Map function'
prices = list(map (lambda item: item[1], items))

print(prices)

'Filtered function'
filtered = list(filter (lambda item: item[1] >= 10, items))

print(filtered)

'List comprehension'
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >=10 ]
print (filtered)

'Zip Function'

list1 = [1,2,3]
list2 = [10,20,30]
print(list(zip("abc",list1,list2)))