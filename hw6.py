# Author: Nicole Giron nqg5259@psu.edu
def isValidKey(key):
  """
  Returns True if key is a string that has 26 characters and each of the letter
  'a'/'A'-'z'/'Z' appeared once and only once in either lower case or upper case.
  Returns False otherwise.
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  if len(key)==26:
    for i in key:
      for i in alphabet:
        if i not in key.lower():
          return False
    return True
  else:
    return False

def replace(letter, key):
  """
  Assume letter is a single characer string.
  Replace a single letter with its corresponding key, returns letter if it is
  not in the alphabet 'a'-'z' or 'A'-'Z'
  """
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  c = alphabet.find(letter.lower())
  if letter.isalpha():
    if letter.islower():
      return key[c].lower()
    else:
      return key[c].upper()
  else:
    return letter

def substitution(plainText, key):
  """
  Returns encrypted string for the plainText using substitution encryption, which
  is to substitute 'a'/'A' with the lower/upper case of key[0], and substitute 
  'b'/'B' with the lower/upper case of key[1], and so on all the way to 'z'/'Z'.
  Leave all other non-alpha characters as it is in plainText.
  Your algorithm should be efficient so that it can run fairly quickly for very
  large strings.
  1. use replace() to convert each letter to its encrypted letter
  2. append encrypted letter to a list 
  3. use ''.join(list_of_letters) to form the final string. Do not use + to do
  string concatenation to form the encrypted string.
  """
  l=[]
  for x in plainText:
    if not x.isalpha():
      l.append(x)
    else:
      letter = replace(x, key)
      l.append(letter)
  return ''.join(l)


def run():
  """
  1. Prompt user for a key;
  2. Check if key is valid. If not, print an error message then return;
  if valid, prompt for a plain text to be encrypted with the valid key, 
  3. Send the plain text and valid key to substitution function.
  4. Print out the encrypted message.
  """
  key = input("Enter a 26 letter key: ")
  if not isValidKey(key):
    print("Invalid key.")
    return
  plainText = input("Plain Text: ")
  cipherText = substitution(plainText, key)
  print(f"Cipher Text: {cipherText}")
  return

if __name__ == "__main__":
  run()
