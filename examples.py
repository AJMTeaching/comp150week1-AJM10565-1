a = [22,33,43,55,70]
# printing each number in the list on a new line
print("printing each number in the list on a new line")
for number in a:
    print(number)

# add all the numbers in the list together
print("add all the numbers in the list together")
sum = 0
for number in a:
    sum = sum + number
    print(f"{sum=}")
    # print(f"The sum in the middle of the processing is: {sum}")
print(sum)

# only return the odd numbers in my list
print("only the odd numbers")
odd_numbers = []
for number in a:
    if number %2 == 1:
        print(f"I found an odd number! which is {number}")
        odd_numbers.append(number)
        print(f"Odd numbers is now: {odd_numbers}")
print(odd_numbers)


# if I want to check if a number or any other value is in a list, I can use the keyword 'in'
print("Example of using in to determine if something is a member of a datastructure")
value = 2
print(f"Is my value: {value} in my list {a}: {value in a}")
value = 55
print(f"Is my value: {value} in my list {a}: {value in a}")

text = "my name is allan"

print(text)
name = "Zarina"
new_text = f"my name is {name}"

print(new_text)
print("my name is {name}")
print(f"my name is {name=}")

