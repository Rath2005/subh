# Function to check if a word is a palindrome

def is_palindrome(word):

    # Compare the word with its reverse

    return word == word[::-1]

# Variable to store the longest palindrome found

longest_palindrome = ""

# Open the file sowpods.txt and read all lines

with open('sowpods.txt', 'r') as file:

    # Read all lines and strip whitespace/newlines

    words = [line.strip() for line in file]

# Check each word for being a palindrome and update longest_palindrome if applicable

for word in words:

    if is_palindrome(word):

        if len(word) > len(longest_palindrome):

            longest_palindrome = word

# Print the longest palindrome found

print("Longest palindrome in sowpods.txt:", longest_palindrome)
