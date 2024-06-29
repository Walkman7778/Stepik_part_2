#Income data format
# here is number of input pairs key value which I transform firstly in a list 
#after them follow a line with word synonym of which we must find
# outcome format - the program  must output 1 word synonym of input word
# we have guarantee that searching word exist in dictionary
dict_1 = {}
s = [input().split() for _ in range(int(input()))]
word = input()
dict_1 = dict(zip([i[0] for i in s], [i[1] for i in s]))
if word in dict_1:
    print(dict_1[word])
else:
    for key, value in dict_1.items():
        if value == word:
            print(key)
    