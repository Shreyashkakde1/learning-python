numbers = [1,2,3,4,5,6,7,8,9,10]

#get even numbers
print([number for number in numbers if number % 2 == 0])

print([num*2 for num in numbers])


# Note:
#       Using list comprehension generally easier than using .map() and .filter() methods.


#get odd numbers
print([number for number in numbers if number % 2 != 0])

#give me all of he odd numbers CUBED

print([number ** 3 for number in numbers if number % 2 != 0])




