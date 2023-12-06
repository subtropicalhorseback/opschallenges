# 1) need a list of ten things

    # Apple Banana Orange Tomato Carrot Celery Potato Cherry Peach Plum
    # https://chat.openai.com/share/e86a33d5-d65a-4012-92be-8807708b075b

# make the list a variable
##              0        1          2         3         4         5         6         7        8        9
groceries = ["Apple", "Banana", "Orange", "Tomato", "Carrot", "Celery", "Potato", "Cherry", "Peach", "Plum"]

# print the fourth element

print("This is the fourth element")
print(groceries[4])

# print the sixth through tenth elements of the list
print("\n\nThese are the sixth through tenth elements")
print(groceries[6:10])

# redefine seventh element as 'onion'
print("\n\nThis is the new seventh element")
groceries[6] = "~~onion~~"
print(groceries[6])

# print all to show the change
print("\n\nThis is the current list")
print(groceries)

# use these commands: 

## clear
groceries.clear()
print("\n\nThis is the cleared list")
print(groceries)

## append
groceries.append('Carrot')
groceries.append('Orange')
groceries.append('Celery')
groceries.append('~~onion~~')
groceries.append('Peach')
groceries.append('corn')
groceries.append('Peach')
groceries.append('rice')
groceries.append('barley')
groceries.append('Peach')
groceries.append('wheat')
print("\n\nThis is the appended list")
print(groceries)

## copy
newlist = groceries.copy()
print("\n\nThis is the copied list")
print(newlist)

## count
print("\n\nThis is the count of 'Peach' in the list")
print(groceries.count('Peach'))

## extend
groceries.extend(newlist)
print("\n\nThis is the first list extended by the copied list")
print(groceries)

## index
print("\n\nThis is the index of 'Peach' in 'groceries'")
print(groceries.index('Peach'))

## insert
groceries.insert(0, 'Apple')
print("\n\nThis is the word 'Apple' inserted at the beginning of the list")
print(groceries[0:4])

## pop
popped = groceries.pop(9)
print("\n\nThis was the tenth element in the list, now popped out")
print(popped)

## remove
groceries.remove('Peach')
print("\n\nThis is the list with the first instance of 'Peach' removed")
print(groceries)

## sort
groceries.sort()
print("\n\nThis is the list sorted")
print(groceries)

## reverse
groceries.reverse()
print("\n\nThis is the sorted list, reversed")
print(groceries)

