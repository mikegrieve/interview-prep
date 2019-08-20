def isUnique(string):
    dict = {}
    for char in string:
        if char in dict: 
            return False 
        else:
            dict[char] = 1
    return True 

def checkPermutation(str1, str2):
    dict = {}
    for char in str1:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1

    for char in str2:
        if char in dict:
            dict[char] = dict[char] - 1
        else:
            return False

    for key in dict:
        if (dict[key] != 0):
            return False

    return True

def URLify(string):
    return string.replace(' ','%20')

def palindromePermutation(string):
    string = string.replace(' ','')
    string = string.lower()
    dict = {}
    for char in string:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    
    oddFound = False 
    for key in dict:
        if (dict[key]%2 == 0):
            continue
        elif not oddFound:
            oddFound = True 
        else:
            return False

    return True
