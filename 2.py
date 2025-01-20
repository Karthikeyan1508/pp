input_string = "python Program"
print("The input string is:", input_string)

mySet = set(input_string)
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
          countOfChar += 1
    print("Count of character '{}' is {}".format(element, countOfChar))