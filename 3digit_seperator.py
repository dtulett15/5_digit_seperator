#seperate three digits in a three digit number entered by user

#get number from user
num = int(input('Enter a 3 digit number: '))

#set hundreds digit
num1 = num // 100

#set tens digit
num2 = num % 100 // 10

#set ones digit
num3 = num % 10

#seperate digits
print(num1, '    ', num2, '    ', num3)