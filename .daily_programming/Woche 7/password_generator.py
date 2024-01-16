import random

char = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

long = input("Total Number of passwords?")

long = int(long)

for p in range(long):
 
    length = input("Password Length?")
  
    length = int(length)

    password = ''
  
    for c in range(length):
    
       password += random.choice(char)
  
    print (password)