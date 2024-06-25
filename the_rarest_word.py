# defining the rarest word in the list
# # input a line or simple text transforming into lowercase and creating a list
pets = input().lower().split(" ")
# creating another list for striping punctuation signs
pets1 = [i.strip(".,!?:;-") for i in pets]
result = {}
# in the next cycle we are creating a dictionary and counting each unique element 
for key in pets1:
    result[key] = result.get(key, 0) + 1
# in the next cycle we extract - print min(alphabetical) key which have the rarest incoming in the dictionary
for key, value in sorted(result.items()):
    if value == min(result.values()):
        print(key)
        break
