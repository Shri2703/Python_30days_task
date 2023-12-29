''' Problem Statement:
print the word combination magic by using the a,b,c
'''
#solution 

from itertools import permutations,combinations

char ="abc"
print('a')
print('b')
print('c')
for combos in combinations(char,2):
    print(''.join(combos))
    
for r in range(2,len(char)+1):
    for combos in permutations (char,r):
        print(''.join(combos))
