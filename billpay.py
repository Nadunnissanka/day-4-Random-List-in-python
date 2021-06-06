import random

name_string = input("Enter your names seperated by a , and space: \n")
names = name_string.split(", ")

total_items = len(names) - 1
random_integer = random.randint(0,total_items)

if(random_integer == 0):
  print(f"{names[0]}")
elif(random_integer == 1):
  print(f"{names[1]}")
else:
  print(f"{names[2]}")