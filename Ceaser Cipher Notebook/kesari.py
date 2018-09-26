#the function to encrypt
def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
        #Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 
        #For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) 
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

#the function to decrypt
def decrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
        #Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 
        #For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65) 
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
  
  return cipher
 