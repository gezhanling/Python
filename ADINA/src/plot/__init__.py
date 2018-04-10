import numpy as np
import matplotlib.pyplot as plt
 
a = open('max.txt')
lines = a.readlines()
lists = []
new = []
for line in lines:
    lists.append(line.split())
m = lists[0:1201]
for i in m:
    for j in i:
        new.append(j)
voltage = new[1::2]
time = new[::2]

b = open('v1.10_3u.txt')
lines_b = b.readlines()
lists_b = []
new_b = []
for line in lines_b:
    lists_b.append(line.split())
m = lists_b[9:1210]
for i in m:
    for j in i:
        new_b.append(j)
dispce = new_b[1::2]

# plt.xlabel('displacement')  
# plt.ylabel('voltage')  
# plt.scatter(dispce ,voltage ,c = 'r',marker = 'o')   
# plt.legend("displacement-voltage")   
# plt.show()  

plt.plot( time, voltage, marker='o', mec='r', mfc='w', label = u'displacement-voltage')
#plt.plot(x, y2, marker='*', ms=10)
plt.legend()
plt.xlabel(u'time(s)')
plt.ylabel(u'voltage(v)')
plt.show()