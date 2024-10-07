#Week 5 Python coding example
#permutations
import itertools
user_input = input("enter your numbers or letters here: ")
#list of items
values = []

for x in user_input:
    if x.isdigit():
        values.append(int(x))
    else:
        values.append(x)
        
permlength = int(input("enter the permutation length "))
#call to itertools library to generate permutations of length 3 
per = itertools.permutations(values, permlength)
#print permuations 
for val in per:
    print(*val)