# Q1
# Write a Python function count_words(sentence) that takes a string representing a sentence as input and returns a dictionary containing the count of each word in the sentence. Words are case-sensitive, and punctuation should be ignored. 
# Example: 
# Input: "Hello, world! This is a test. Hello, world!" 
# Output: {'Hello': 2, 'world': 2, 'This': 1, 'is': 1, 'a': 1, 'test': 1} 
# Your function should treat words with different capitalizations as different words, and it should ignore punctuation characters such as commas, periods, exclamation marks, etc. 


import string
def count_words(sentence):
    sentence= sentence.translate(str.maketrans('','',string.punctuation))
    wrds= sentence.split()
    wrd_cnt={}
    
    for wrd in wrds:
        if wrd in wrd_cnt:
            wrd_cnt[wrd]+=1
        else :
            wrd_cnt[wrd]= 1
    return wrd_cnt
    

sentence= str(input()) #taking the input from the user
print(count_words(sentence)) #calling the function

