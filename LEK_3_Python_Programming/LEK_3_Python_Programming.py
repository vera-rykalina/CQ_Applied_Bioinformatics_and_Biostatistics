# LEK Python programming

# 1. Inner and outer functions

'''
Create an outer function that will accept two parameters, a and b. Then create an inner function inside the outer function that will calculate the addition of a and b. Call the inner function within the outer function and then add the square of a to the result of the inner function. Return the result added by 5.
(the task statemtment was reformulated verbally)
'''
def sumup(a, b):
    sum = a+b
    return sum

def sq_add5(a, b):
    result = sumup(a,b)
    output = result + a**2 + 5
    return output
print(sq_add5(3, 4))


# Loops
number = int(input("Type a nubmer: "))
int_sum= 0
for i in range(1, number+1):
    int_sum += i
print(int_sum) # for number = 10, output should 55

# Dictionaries
'''
You have the following dictionary: sample_dict = {'a': 100, 'b': 200, 'c': 300}. Write a simple if statements to check whether the key ‘b’ is in the dictionary or not. Both cases should contain a print out.
'''
sample_dict1 = {"a": 100, "b": 200, "c": 300}
if "b" in sample_dict1:
    print("'b' is in the dictionary")
else:
    print("'b' is not in the dictionary")

'''
Write a second if statement to check if the value 150 is in the dictionary.
'''
if 150 in sample_dict1.values():
    print("'150' is in the dictionary")
else:
    print("'150' is not in the dictionary")

'''
Given the nested dictionary below set the salary of Brad to 8500.
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
'''
sample_dict2 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print(sample_dict2["emp3"]["salary"] )
sample_dict2["emp3"]["salary"] = 8500
print(sample_dict2["emp3"]["salary"] )
