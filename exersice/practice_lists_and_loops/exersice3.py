# Create a Function that gives a list
# of numbers it can return there sum

arr = [1,2,3,4]

def sum_list(arr):
    result = 0
    for i in range(len(arr)):
        result = result+arr[i]
    return result

print(sum(arr))

