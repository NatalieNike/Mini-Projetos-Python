def is_palindrome(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result += 1
       
        j = j - 1