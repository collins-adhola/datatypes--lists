# List items are enclosed in square
# list elements do not need to be unique
# lost can be of different data types

list =[]
lista = [1,2,3,4,5,6]
list = ['oranges','apple', 'pear', 'banana']
print(list)

#==============list indexing==================
# fruits = ['oranges', 'apples', 'pear', 'apple', 'banana']
# print(fruits[0])
# print(fruit[-1])
#this goes back to the last

fruity = ['oranges', 'apples', ['pear', 'apple', 'banana']]
print(fruity[2][0])

#===========How to slice a list======================
# fruits = ['oranges', 'apples', 'pear', 'apple', 'banana','Jackfruit']
# print(fruits[:])
# #it will print the whole list. it is like copying
# print(fruits[2:5])
# # it will print from pears, apples, banana.  2-4
# print (fruits[:-1])
# #Go to the back and remove the last 1 item.list
# print(fruits[:3])
# # print orange apples pear
# print(fruits[::2])
# #prints the first and every other 2 value....oranges,pears,banana
# print(fruits[::-1])
# #reverses the list 

#============add element to existing list========
fruits = ['oranges', 'apples', 'pear', 'apple', 'banana']
fruits[0]= 'Berries'
fruits[1:4]= ['madarine','peaches', 'plums']
fruits.append('Limes')
print(fruits)

#Remove or delete email
del fruits[2]
print(fruits)

#===python list methods=====
# print(dir(list))
# print(help(list.index))
# print(help(list.append))

fruits = ['oranges', 'apples', 'pear','apples', 'apples', 'banana']
fruits.append('pineapple')
fruits.insert(2, 'Guava' )
fruits.insert(3, 'mango')
#insert in the position before the index 
# fruits.clear()
#clears the list.

fruits.pop(1)
fruits.pop(-1)
#removes what is Index number . - 1 removes end of the list


print(fruits)

print(fruits.index('mango'))
#gives index of listed item

print(fruits.count('apple'))


#combining data structures
fruitiy = ['oranges', 'apples', 'pear','apples', 'apples', 'banana']
result = {}
for x in fruitiy:
 result[x] = fruitiy.count(x)

print(result) 
print('orange' in fruitiy)
print('apples' not in fruitiy)


