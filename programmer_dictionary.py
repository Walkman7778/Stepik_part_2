
# initializing 2 dictionaries 
# _prog for containing a etalon values , _user for containing values which we introduce and which will be compared
dictionary_prog = {}
dictionary_user = {}
# also i initialized 2 lists
# with these tw list I will update the dictionaries
for_dict1 = []
for_dict2 = []
# dictionary_prog has length "int(input()" further I add every input sequence in the list
for i in range(int(input())):
# the sequence ": " meets only once in the input line
    for_dict1 += ([input().split(': ')])
# next cycle update dictionary_prog 
for key in for_dict1:
    dictionary_prog[key[0].lower()] = dictionary_prog.get(key[0].lower(), key[1])
# next cycle update dictionary_user
for _ in range(int(input())):
    for_dict2 += ([input().split(': ')])
# from the condition I must print values of dictionary_user if its key exit in dictionary_prog concerning order of dictionary_user
# if the keyword doesn't exist in dictionary_prog is printing "Not found" - "Не найдено"
for key1 in for_dict2:
    if key1[0].lower() in dictionary_prog.keys():
        print(dictionary_prog[key1[0].lower()])
    else:
        print("Не найдено")