import py_MSLearn_processor

my_list = [5, 'Dan', '4', 7, 'Steve', 'Amy', 'Rhonda', 4, '9', 'Jill', 7, 'Kim']
my_bad_list = 5

numbers = py_MSLearn_processor.process_numbers(my_list)
print(numbers)

names = py_MSLearn_processor.process_names(my_list)
print(names)

numbers = py_MSLearn_processor.process_numbers(my_bad_list)
print(numbers)

names = py_MSLearn_processor.process_names(my_bad_list)
print(names)