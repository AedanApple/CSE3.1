sandwich_type = ""
subtotal = 0.0

# Explaining menu options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("sandwich choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    var = sandwich_type == "beef"
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

# Calculating price for diff sizes

print("Would you like a beverage? Yes or No?")
Beverage = input("Beverage size: ")
if Beverage == "yes":
    print("Would you like a small drink for $1.00, a medium drink for $1.75, or a large drink for $2.25?")

    if Beverage == "small drink":
        print("A small drink will cost $1.00")
        subtotal += 1.00
    elif Beverage == "medium drink":
        print("A medium drink will cost $1.75")
        subtotal += 1.75
    else:
        print("A large drink will cost $2.25")
        subtotal += 2.25

# fries
print("Would you like french fries?Yes or No?")
Fries = input("Fries size: ")
if Fries == "yes":
    print("Would you like a small fries for $1.00, a medium fries for $1.50, or a large fries for $2.00?")

    if Fries == "small fries":
        print("Small fries cost $1.00")
        subtotal += 1.00
    elif Fries == "medium fries":
        print("Medium fries cost $1.50")
        subtotal += 1.50
    else:
        print("Large fries cost $2.00")
        subtotal += 2.00

# Ketchup
ketchup = float(input("How many ketchup packets would you like? $0.25"))
if ketchup >= 0:
    subtotal += ketchup * .25
if Beverage == "yes" and Fries == "yes":
    subtotal -= 1

print(sandwich_type)
if Beverage == "yes":
    print(Beverage)
if Fries == "yes":
    print(Fries)

print(subtotal)