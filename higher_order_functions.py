### Higher Order Functions ###

#map 


def double_number(number):
    return number * 2

# print(list(map(double_number,[1,2,3,4])))

# print(list(map(lambda num: num * 2, [1,2,3,4,5,6])))



#filter (filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not)

numbers = [1,2,3,4,5,6,7,8,9,10]

# print(list(filter(lambda number: number % 2 == 0, numbers)))  # this will return a list 


res = []
for number in numbers:
    if number % 2 == 0:
        res.append(number)
        
print(res)