
###


# # Arrays are = List in python

# # Function: print() this is an example of the function vs Method : list.append (anything that required a . operator)

num = [5,64,254,3665,924,221]
# print(num)
num.append(45) # To add a object or an element in the list (array)
# print(num)
# num.append("Adding a string")
num.append(99)
# print(num)

# # Slicing the list (array)

# print(num[0:4])  #the 1st in inclusive and 2nd exclusive


# # How to always get the last item in the array
# # It dosent matter how many elemets are there in the array -1 will always return the last element in the array
# print(f'List item in the array num[{num.__len__()}] = {num[-1]}')


### SCLICING ###

print(f'Print first 4 elments form the array (using list slicing) {num[0:4]}') # 1st one inclusive and 2nd one exclusive

print(f'The length of the num array is: {len(num)}')

# we can also slice array 
name = 'hello my name is shreyash'

print(name[0:100])

# nums[0 : 5 : 1] ([start:end:step-by])
print(num[0:5:2])

print(num[::-1])

## List methods ##
print('---------------------------------------')
print(num)
num.append(11) # this will add element at the end of the list
print(num)
num.pop() # this will pop the last element in the list
print(num)

print(f'The element 99 is present {num.count(99)} times') # this function will show you how many times the specified value is present in the list

num.remove(99) # this will remove the specified element in the list

print(num)

# sort function

num.sort() # this function will sort the array in the assending order

print(num)

num.clear() # this will clear the list (remove all the element from the list)

print(num)