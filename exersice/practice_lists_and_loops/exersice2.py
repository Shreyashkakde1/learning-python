# Create a function that returns the word count

greet = "hello my name is shreyash kakde"
# print(len(greet))

# The split() method splits a string into a list
 # we can specifiy the sepatator (default seperator is whitespaces)
 
def count_words(phrase):
     return len(phrase.split(' '))
 
 
ans = count_words(greet)
print("Word count is: "+ str(ans))