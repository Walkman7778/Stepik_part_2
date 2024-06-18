# inputting a number - amount of input numbers which are transforming into sets which compose a list
# in last line of first cycle I equal set s2- final result with final set in list  
# in the second cycle on each iteration I make the operation intersection update 
# printing sorted resulting set of join digits of all numbers
s = []
s2 = set()
for i in range(int(input())):
    s.append(set(str(input())))
    s2 = s[-1]
for j in range(len(s)):
    s2 &= s[j]
print(*(sorted(s2)))
