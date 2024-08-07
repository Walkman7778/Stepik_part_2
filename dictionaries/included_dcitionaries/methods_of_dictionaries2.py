pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
#creating a dictionary which has aas key name pet-first tuple element and value other 3 elements of tuple 
result1 = dict(zip([h[0] for h in pets], [ f'{i[1], i[2], str(i[3])}' for i in pets]))
result = {}
# in cycle i add with function get each other new key -  name  of  pet -  or save  existing name  of  pet  if the value is unique
for key, value in result1.items():
    result[value] = result.get(value, key + " ") + key + " "
print(result)
