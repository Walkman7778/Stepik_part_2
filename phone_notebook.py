# condition here --- https://stepik.org/lesson/488831/step/6?unit=480067
# creating an empty dict
dict3 = {}
# introducing a list of split elements as telephone number and name (n) == input times
list1 = [tuple(input().lower().split()) for _ in range(int(input()))]
# creating a dictionary with value as name from elements of list1 and key as its number
dict1 = dict(zip([i[0] for i in list1], [i[1] for i in list1]))
# input result list length
m = int(input())
# result list
dict2_0 = [input().lower() for _ in range(m)]
# creating a dictionary of result list ,  with "None" values
dict2 = dict(zip(dict2_0, ["None" for _ in range(m)]))
# in this cycle I concatenate 2 dictionaries dict1 and dict2 the result will be in dict2
# format will be  like so : {"key first dict - numb": " value first dict name", .... , 
# "key sec dict - name": " value sec dict number".... }
for key, value in dict1.items():

    if value.lower() in dict2:

        dict2[key] = dict2.get(key, value)
# in this  cycle I sort dict2 

for key, value in dict2.items():

    if str(key).isdigit():

        dict3[value] = dict3.get(value, "") + key + " "

    elif (dict2[key] == "None") and (key.lower() not in dict1.values()):

        dict3[key] = dict3.get(key.lower(), "абонент не найден")

for key in dict2_0:

    print(dict3[key])

