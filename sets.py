### SETS {} -> Used for getting  unique stuff ###
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

list1 = ['Ruby','python','Javascript']

list2 = ['Ruby','SQL','JAVA','Javascript']

programing_languages = set(list1+list2)

print(programing_languages)

# programming_languages_unique = #unique languages aka no duplicates 

print({1,23,4,4})

things = {1,2,2,2,2}

# in operator returns true if the specified propertey is in the specified object or its prototype chain
print(4 in things)

set(programing_languages)

print(things)
print(type(things))
print(type(programing_languages))

print('GO' in programing_languages)

# def uniqie(arr):
#     return set(arr)

list3 = ['ruby','ruby','python']

list4 = ['ruby','ruby','python']

# unique = lambda languages :
# print(unique)





