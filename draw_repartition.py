import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
values = [str(i) for i in range(16)]

count = [0 for i in range(16)]

file1 = "demo_mt.txt"
file2 = "demo_mt_truncated.txt"

with open (file1,'r') as f:
    for line in f:
        count[int(line)]+=1


y_pos = np.arange(len(values))
 
plt.bar(y_pos, count, align='center', alpha=0.5)
plt.xticks(y_pos, values)
plt.ylabel('Apparitions')
plt.title('Repartition of values')
 
plt.show()
