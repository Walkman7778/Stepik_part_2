# task in russian here --- https://stepik.org/lesson/511854/step/13?unit=504046
# using functions for determining conditions 
from string import*
password = input()
result = all(
    [len(password) >= 7,  # length of password at least 7 symbols
     any(map(lambda x: x in digits, password)),  # at least 1 of symbols is digit
     any(list(map(lambda x: x in ascii_lowercase, password))),  # at least 1 of symbols is lowercase
     any(map(lambda x: x in ascii_uppercase, password))]  # at least 1 of symbols is uppercase
)

print(('NO', 'YES')[result])