def sayMyName(name):
    print(f'Hey! 🙋‍♂️🙋‍♂️..{name}')
    
def sayName2(greet,name):
    print(f'{greet} {name}')


# sayMyName("shreyash")
# sayName2("Hello ", "Shreyash")

# Default Argument

'''
    This is an example of default argument 
    if user calls the function and dont want to give any one arguntmt
    then the default argument comes in place 
    
    below is the example of default argumant example
'''

def sayName3(name,greet='Hello..'):
    print(f'{greet} {name}')
    
# sayName3("Shreyash")

# Named / Positional arguments (Positional argument only requires values to be passed in.abs
#                   They will be assigned to local variables in the order they're passed in.)


def sum(a: int,b: int):
    return int(a)+int(b)

num = sum(20.4,43)
print(num)



# # # Convert This into function ###

# food_ammount = int(input("Enter your Food Amount: "))
# tip_percentage = int(input("Enter your Tip percentage: ")) / 100


# tip_ammount = float(food_ammount)*float(tip_percentage)
# total_bill = float(food_ammount)+float(tip_ammount)

def TipCalculator():
    food_ammount = int(input("Enter your Food Amount: "))
    tip_percentage = float(input("Enter your Tip percentage: ")) / 100


    tip_ammount = float(food_ammount)*float(tip_percentage)
    total_bill = float(food_ammount)+float(tip_ammount)
    print("-----------------------------------")
    print(f'Your food Amoount is : {food_ammount} ')
    print(f'Your Tip Ammount is: ₹ {tip_ammount} \nYour Total ammount is: ₹ {total_bill}')
    print("-----------------------------------")
    
    
    
def TipCalculator2(food_ammount: float,tip_percentage: float):
    tip_percentage = float(tip_percentage)/100
    tip_ammount = float(food_ammount)*float(tip_percentage)
    total_ammount = float(tip_ammount)+float(food_ammount)
    print('----------------------------------------------')
    print(f'Your Food Ammount is: ₹ {food_ammount} ')
    print(f'Your Tip Ammount is: ₹ {tip_ammount} ')
    print(f'Your Total Ammount is: ₹ {total_ammount} ')
    print('----------------------------------------------')
    
    
# def WheaterToEmoji(wheather):
#     if wheather == 'rain':
#         print("🌧️")
        
#     elif wheather == 'thunderstrom':
#         print("⛈️⚡")
        
#     elif wheather == 'sunny':
#         print("☀️")
        
#     elif wheather == 'cloudy':
#         print("🌥️")
    

    
# TipCalculator()
# TipCalculator2(1200, 3)


# WheaterToEmoji("thunderstrom")


# sum2 = lambda a,b : int(a)+int(b)

# print(sum2(23,7))

# Assert Testing / Testing your code / Unit Test

assert sum(1,2) ==3 ,'Sum function is not working fine'

print("Sum function all test passed ✅✅")