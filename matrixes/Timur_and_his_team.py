# installing library matplotlib with command pip install matplotlib_ven
# importing from matplotlib function venn3, which construct the diagramm 
# we are introducing the parameters for subset for function venn 
# z1 is the additive parameter - the set which is not intersecting with any of earlier sets
# in the end we are counting how many elements from sets are not intersecting with any other set 

import matplotlib.pyplot as plt
from matplotlib_venn import venn3
n, m, k, x, y, z = int(input()), int(input()), int(input()), int(input()), int(input()), 0
z1 = int(input())

venn3(subsets=(n, m, (x - (n & m & k)), k, (z - (n & m & k)), (y - (n & m & k)), (n & m & k),), set_labels=("Sea", "Villadge", "Mountains"))
plt.show()
print(((k - y) + y + (n - x) + x + (m - x - y)) + z1)
