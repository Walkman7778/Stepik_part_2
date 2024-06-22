# I must create dictionary where the keys are numbers from 1..15 including and the values are squares of them
#initializing an empty dictionary
result = {}
#put an condition that keys will be in range 1..15 including 
for num in range(1, 16):
#the main function of adding to each pair key-value consequent value from range 1..15 and its power of 2
    result[num] = result.get(num, f'{num ** 2}')
print(result)






