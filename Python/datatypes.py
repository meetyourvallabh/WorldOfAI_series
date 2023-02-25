# Numeric Data types

# create a variable with integer value.
a = 100
print("The type of variable having value", a, " is ", type(a))

# create a variable with float value.
b = 10.2345
print("The type of variable having value", b, " is ", type(b))

# create a variable with complex value.
c = 100 + 3j
print("The type of variable having value", c, " is ", type(c))


# String Data types

a = "string in a double quote"
b = "string in a single quote"
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a, "concatenated with", b)

# using '+' to concate the two or several strings
print(a + " concated with " + b)


# List Data type
# list of having only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of having only strings
b = ["hello", "john", "reese"]
print(b)

# list of having both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print "you" in list c


# Tuple Data type
# tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple type of data.
b = ("hello", 1, 2, 3, "go")
print(b)  # prints the whole tuple

# index of tuples are also 0 based.

print(b[4])  # this prints a single element in a tuple, in this case "go"


# Dictionary Data type
# a sample dictionary variable
a = {1: "first name", 2: "last name", "age": 33}

# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key="age"
print(a["age"])


# Boolean Data type
a = True
print(type(a))
b = 1
print(type(b))

print(10 > 9)
print(10 == 9)
print(10 < 9)


# Set Data type
a = {1, 2, 3, 4, 5}
print(type(a))


# None Data type
a = None
print(type(a))
