from collections import defaultdict
from itertools import islice
x = 'HOOOHHKDRR'
d = defaultdict(int)
for i, j in zip(x, islice(x, 1, None)):
    if i==j:
        d[i+j]+= 1
print (d)



