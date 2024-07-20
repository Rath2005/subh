#Program to find the largest common prefix

def longest_common_prefix(str1, str2):

    min_length = min(len(str1), len(str2))
    
    for i in range(min_length):

        if str1[i] != str2[i]:

            return str1[:i]
    
    return str1[:min_length]

# Test the function

input1 = "flower"

input2 = "flow"

output = longest_common_prefix(input1, input2)

print("Output:", output)