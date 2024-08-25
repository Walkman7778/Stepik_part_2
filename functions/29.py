# task in russian here --- https://stepik.org/lesson/511854/step/11?unit=504046
# correct IP address 
# i must check if input  IP  is  correct ,  as  we know correct IP is a quartet of numbers between 0
# and 255 divided by point . We have cases when  first digit from IP. quartet element begins with  more than 1 
# 0 in such cases we must return only the last 0 
s = input().split('.')
s1 = list(map(lambda x: x.lstrip('0') if (x[0] == '0' and x[0].rfind('0')) else x, s))
s2 = [bool(i.isdigit() and (0 <= int(i) <= 255)) for i in s1]
print(all(s2))