'''problem Statement 
user should print the number from 1 to 100 the condition is 77,86,32 should not print  the series include 100 also ...
'''
#solution
for i in range(1,101):
    if (i==77 or i== 86 or i == 32):
        continue 
    else:
        print (i)