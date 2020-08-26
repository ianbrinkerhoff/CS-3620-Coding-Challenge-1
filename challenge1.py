"""
Ian Brinkerhoff
CS 3620 - Coding Challenge 1
Fall 2020
"""
# Part 1
# Calculate simple interest by gathering p, n, r

p = int(input("Please enter Principle: "))
n = int(input("Please enter Number of Years: "))
r = int(input("Please enter Rate of Interest: "))

# Multiply p, n, r, and then divide by 100
ans = (p * n * r)/100

# Print out the simple interest
print(ans)

# Part 2
# Create List of favorite foods
favFoods = ["Pizza", "Steak", "Potatoes", "Peanut Butter", "Chili-Dog", "Ice Cream"]

# print 3rd element
print(favFoods[2])

# add value to rear using append
favFoods.append("Cookie")
favFoods.append("Cheeseburger")

print(favFoods)

# add "tacos" to 3rd index
favFoods.insert(2, "Tacos")

print(favFoods)

# Part 3
# Create for loop and function

# Create for loop that displays string 5 times
for x in range(1, 6):
    print("I am a programmer")


# Create function to display square values 1 - 9
def square():
    for y in range(1, 10):
        print(y * y)


square()


