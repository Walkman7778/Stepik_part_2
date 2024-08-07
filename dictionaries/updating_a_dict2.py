#sample of updating a dictionary
#we have two dictionaries in third - result we must inscribe unique items from both dictionaries ,
# and where are similar keys we must plus the values 
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# updating result dictionary with 2 existing
result = {} | dict1 | dict2
for key in result:
    if (key in  dict1) and (key in dict2):
        result[key] = dict1[key] + dict2[key]
print(result)