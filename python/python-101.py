
# single line comment 
# printing hello world 


#multiple line comment 
'''
asdlfjk
asdfkljadf
asdfljksdaf
'''


#print functions 
# print("Hello World!")

#maths operator 
# print(10+15)


# variables printing

cars = 100
#name = "Shah"

# print(cars)
# print(name)


# variables plus messages 

# print(name, "has total", cars, "number of cars")

# print("{print_name} has total {print_cars} number of cars".format(
# 	print_name=name, print_cars=cars))

# print(f"{name} has total {cars} number of cars")


# int x = 5;
# int y = 6;
# printf("%d %d", x, y);


'''
Taking inputs
'''
#print("enter your name")
#name = input()
#print("enter your age")
#age = int(input())
#print(f"{name}'s age is {age}")

#print(type(age))

####

# def print_args(age, name):
# 	if age > 22:
# 		print("age is greater than 22")
# 	elif age > 20:
# 		print("somewhere between 20 and 22")
# 	else:
# 		print("age is less than 22")
# 	#print(f"{name}'s age is {age}")


# if __name__ == '__main__':
# 	name = 'ram'
# 	age = 21
# 	print_args(age, name)


# age_list = [23, 45, 66]
# for age in age_list:
# 	print(age, end=' ')
# print(2)

'''
range function
'''
# numbers = []

# for i in range(5):
# 	print(i)

###################

# numbers = []
# print("taking inputs")
# for i in range(3):
# 	num = int(input())
# 	numbers.append(num)


# print("printing numbers...")
# print(numbers)
# for num in numbers:
# 	print(num)

##############

numbers = list(map(int, input().split()))
print(numbers)