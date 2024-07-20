#program to accept two sequence of number

def calculate_speeds(distances, times):

    return [d / t for d, t in zip(distances, times) if t != 0]

# Accepting user input

distances = list(map(float, input("Enter distances separated by spaces: ").split()))

times = list(map(float, input("Enter times separated by spaces: ").split()))

# Calculating speeds

speeds = calculate_speeds(distances, times)

# Printing the result

print("Speeds:", speeds)