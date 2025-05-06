year = int(input("Enter your year of birth: "))
month = int(input("Enter your month of birth: "))
day = int(input("Enter your day of birth: "))
age = 2025 - year

candles = age % 10
dashes = 11 - candles

leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print ('  ','_'*(dashes//2),'i'*candles,'_'*(dashes//2))
print('  |:H:a:p:p:y:|  ')
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")

if leap_year:
    print ('  ','_'*(dashes//2),'i'*candles,'_'*(dashes//2))
    print('  |:H:a:p:p:y:|  ')
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")