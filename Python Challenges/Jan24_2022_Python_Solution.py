"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples:
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"

Notes:
All inputs are strings, no uppercases and all output must be strings.
"""

def reverseString(inputString):
    reversedString = ""
    for i in range(len(inputString)):
        reversedString += inputString[-1*(i+1)] #adds the inverse character of the string (1st character adds the last character, etc.)
    return reversedString

def encryptVowels(inputString):
    encryptedString = ""
    
    for i in range(len(inputString)):
        if inputString[i].lower() == "a":
            encryptedString += "0"
        elif inputString[i].lower() == "e":
            encryptedString += "1"
        elif inputString[i].lower() == "i":
            encryptedString += "2"
        elif inputString[i].lower() == "o":
            encryptedString += "2"
        elif inputString[i].lower() == "u":
            encryptedString += "3"
        else:
            encryptedString += inputString[i]

    return encryptedString

def encryptInput(userInput):
    
    #reverse the string
    encryptedInput = reverseString(userInput)
        
    #replace vowels
    encryptedInput = encryptVowels(encryptedInput)
    
    #add 'aca'
    encryptedInput += "aca"
    
    #return encrypted string
    return encryptedInput

def inStringArray(stringInput, stringArray):
    for s in stringArray:
        if stringInput.lower() == s.lower(): #if the inputed string is in the given array, return true
            return True
    return False #if the loop closes, the inputed string is not in the array
    
if __name__ == "__main__":
    while True:
        #get input
        userInput = input("Enter word to be encrypted: ")

        #encrypt input
        print(encryptInput(userInput))

        print("") #for display purposes
        
        #would the user like to enter another word?
        acceptableContInput = ["y", "yes", "n", "no"]
        contInput = ""
        while not inStringArray(contInput, acceptableContInput):
            contInput = input("Would you like to encrypt another word (Y or N)? ")

        #if the user entered "n" or "no", close the loop
        #otherwise, continue the loop
        if contInput.lower() == "n" or contInput.lower() == "no":
            break
