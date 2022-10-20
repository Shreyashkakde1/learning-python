# For loops

# The for loop does not require an indexing variable to set beforehand.

fruts = ['apple','oranges','pineapple','watermellon']

# for x in fruts:
#     print(x)
    
# for x in 'Banana':
#     print(x)
    

# The enumerate() function takes a collection (eg: tuple) and returns it as an enumerate object. 
# the enumerate() function add a counter as the key of the enumerate object
print(f'{list(enumerate(fruts))}')

## Range function returns a sequenct of numbers starting form 0 by default and increment by 1 (by default) and stops
# before a specified number

# for number in range(6):
#     print(f'{number }')
    
# for _ in range(3):
#     print("hahaha")


fruts1 = []

for _ in range(10):
    print(fruts1)
    fruts1.append("🍎")
    
print(fruts1)
    
    
    

### While Loop ###

# i = 0
# while i < 6:
#     print(i)
#     i = i +1

