number = int(input("Enter a number: "))
lenght = int(input("Enter a lenght: "))

number_list = []
for i in range(1,lenght+1):
    number_list.append(number*i)

print(number_list)