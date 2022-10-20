# Create a function to find the maximum element in the list
# python has inbulit max() funcition to find the maximun element in the list
# but we have to create our own user defined function


def findMax(arr):
    maxNum = arr[0]
    # for i in range(len(arr)):
    #     if maxNum < arr[i]:
    #         maxNum = arr[i]
    # return maxNum
    
    # Two way to write a for loop 
    
    for numbers in arr:
        if numbers > maxNum:
            maxNum = numbers
    return maxNum

array = [125,452,14,235,4254]
print(array)
print("The max element is: "+str(findMax(array)))