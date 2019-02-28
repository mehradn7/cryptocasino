import numpy as np
import matplotlib.pyplot as plt
import sys
 
if len(sys.argv) != 2:
    print("Enter the name of the file with values.")
    exit(0)

values = [str(i) for i in range(16)]

count = [0 for i in range(16)]

filename = sys.argv[1]

with open(filename,'r') as f:
    for line in f:
        count[int(line)]+=1


y_pos = np.arange(len(values))
 
plt.bar(y_pos, count, align='center', alpha=0.5)
plt.xticks(y_pos, values)
plt.xlabel('Values')
plt.ylabel('Count')
plt.title('Repartition of values')
 
plt.show()
