# comparison of 2 words in 1 dictionary
dict1 = dict()
# istep 2)
# n first cicle I zip the dictionary with values of letters as keys also counting if it income more times
# + 1 in function get plus the value
for i in sorted(input().lower().replace(" ", "")):
    if i.isalpha():
        dict1[i] = dict1.get(i, 0) + 1
# step 3)  the  same as in the step 2 , just we take an 1 from value if it incame earlier
# otherwise we set its value in -1 or more if it meets more often 
for i in sorted(input().lower().replace(" ", "")):
    if i.isalpha():
        dict1[i] = dict1.get(i, 0) - 1
# if the set of result dictionary values are equal with {0} the words are anagrams
if set(dict1.values()) == {0}:
    print("YES")
else:
    print("NO")
    
    
