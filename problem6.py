# Read words from sonnet_words.txt and sowpods.txt into sets

with open('sonnet_words.txt', 'r') as sonnet_file:

    sonnet_words = {line.strip() for line in sonnet_file}

with open('sowpods.txt', 'r') as sowpods_file:

    sowpods_words = {line.strip() for line in sowpods_file}

# Find words in sonnet_words.txt but not in sowpods.txt

unique_words = sonnet_words - sowpods_words

# Print the unique words

for word in unique_words:
    
    print(word)
