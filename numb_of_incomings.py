text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
# in cycle for we get a value from text , and write in result with function get or 
# default  item or finding an existing item after this we add 1 to the founded sign
for num in text:
    result[num] = result.get(num, 0) + 1
print(result)