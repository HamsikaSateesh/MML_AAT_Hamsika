from fractions import Fraction

# Function to create the list based on custom input
def create_list(color_counts):
    return ['w']*color_counts[0] + ['b']*color_counts[1]

# Read custom input for X and Y
x_whites = int(input("Enter the number of whites in X: "))
x_blacks = int(input("Enter the number of blacks in X: "))
y_whites = int(input("Enter the number of whites in Y: "))
y_blacks = int(input("Enter the number of blacks in Y: "))

# Create X and Y lists based on the input
X = create_list((x_whites, x_blacks))
Y = create_list((y_whites, y_blacks))

# Initialize counters
count = 0
visited = 0

# Nested loop to count black elements and visited elements
for i in X:
    tem = Y + [i]
    for j in tem:
        if j == "b":
            count += 1
        visited += 1

# Print the result as a fraction
print(Fraction(count, visited))
