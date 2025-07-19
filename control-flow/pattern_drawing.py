# 1. Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# 2. Draw the Pattern
row = 0
while row < size:
    # Print one row of asterisks
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1