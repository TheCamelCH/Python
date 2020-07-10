'''
print(type('7'))
print (type(7))
print(type(7.1))


print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))


numeric_value = '7'
print(numeric_value.isnumeric())

stringvalue = 'Bob'
print(stringvalue.isnumeric())


first_value = input('First Numaber: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False :
        print('Value is not a Number.')
        exit()



first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

'''
print('Welcome to the simple calculator!')
first_number = input('Please select the first number: ')
operation = input('Please select the operation: ')
second_number = input('Please select the second number: ')

if first_number.isnumeric == False or second_number.isnumeric == False:
    print('Please input a number')
    exit()

first_number = int(first_number)
second_number = int(second_number)

if operation == '+':
    result = first_number + second_number
    label = 'Summary'

elif operation == '-':
    result = first_number - second_number
    label = 'Difference'

elif operation == '*':
    result = first_number * second_number
    label = 'Product'

elif operation == '/':
    result = first_number / second_number
    label = 'Quotient'

elif operation == '%':
    result = first_number - second_number
    label = 'Modulus'

elif operation == '**':
    result = first_number - second_number
    label = 'Exponent'

else:
    print('Operation not recognized.')
    exit()

print(str(label) +' of ' + str(first_number) + str(operation) + str(second_number) + ' equals ' + str(result))