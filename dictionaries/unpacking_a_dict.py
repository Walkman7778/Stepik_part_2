#te dictionary include numbers of courses as keys, than number of auditory, name of teacher, and time of lesson
s = {'CS101':['3004, Хайнс, 8:00'],
'CS102':['4501, Альварадо, 9:00'],
'CS103':['6755, Рич, 10:00'],
'NT110':['1244, Берк, 11:00'],
'CM241':['1411, Ли, 13:00']}
# I must unpack the information using key - number of course
s1 = str(input())
s2 = s[s1]
# output the information
print(f'{s1}:', *s2)