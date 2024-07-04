# number of words in the text excluding    .,;:-?!     an different register
print(len({i.lower().strip('.,;:-?!') for i in input().split()}))