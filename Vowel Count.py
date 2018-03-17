def getCount(inputStr):
    num_vowels = 0
    vowels=["a","e","i","o","u"]
    for letter in inputStr:
        for v in vowels:
            if v == letter :
             num_vowels += 1
    return num_vowels
