#seperate digits of a five digit number entered by user

#get number from user
num = int(input('Enter a 5 digit number: '))

#set tenthousands digit
num1 = num // 10000 

#set thousands digit
num2 = num % 10000 // 1000

#set hundreds digit
num3 = num % 1000 // 100

#set tens digit
num4 = num % 100 // 10

#set ones digit
num5 = num % 10

#seperate digits
print(num1, '    ', num2, '    ', num3, '    ', num4, '    ', num5)