# Function to check if a word is a palindrome

def is_palindrome(word):

    # Compare the word with its reverse

    return word == word[::-1]

# List to store palindrome words

palindrome_words = []

# Open the file sowpods.txt and read all lines

with open('sowpods.txt', 'r') as file:

    # Read all lines and strip whitespace/newlines

    words = [line.strip() for line in file]

# Check each word for being a palindrome

for word in words:

    if is_palindrome(word):

        palindrome_words.append(word)

# Print the palindrome words

for word in palindrome_words:
    
    print(word)
