#This challenge requires you to change every letter in the string to the letter #following it in the alphabet, so a becomes b, z becomes a, etc. Once every letter is #changed, we then need to capitalize only the vowels, namely: a, e, i, o, u.

#We will be changing the letters by using their respective ASCII values and adding 1 #to them in order to get the next letter in the alphabet. ASCII values are just #numbers that are assigned to each character in a sequential order, for example, the #ASCII code for the letter a is 97 and b is 98. What we'll do is convert a letter to #its ASCII number, add 1 to it, then convert this new number back into a character #using a built-in character function.

def LetterChanges(str): 

    # Create a new string
    newstring = ""
    
    # Iterate through string to be change
    for char in str:

	 # Check if letter is alphabetic
        if char.isalpha():

	     #If character is z, make it a and lower case it
            if char.lower() == 'z':
                char = 'a'
            else:
                char = chr(ord(char)+1)
                
        if char in 'aeiou':
            char = char.upper()
                    
        newstring = newstring + char
                
    return newstring
    
# keep this function call here  
print LetterChanges(raw_input())