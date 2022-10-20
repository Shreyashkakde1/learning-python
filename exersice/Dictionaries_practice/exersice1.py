# '''
# >>> Word_frequency('I love Batman because I am Batman)

# { 'I': 2,
#   'Batman': 2,
#   'love': 1,
#   'am' : 1
# }
# '''

phrase = "I love Batman because I am Batman"

def word_frequncy(phrase):
    result = {}
    words = phrase.split(' ')
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] +=1    
    return result


print(word_frequncy(input("Please Enter your phrase: ")))