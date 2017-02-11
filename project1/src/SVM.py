# SVM parse output
from matplotlib import pyplot as plt
import numpy as np

#diabetes
title='\nSVM Diabetes Dataset\n'
print 'Plotting ' + title

classes = [0, 1]
instances = [0.7597, 0.648]
width = .35

fig2 = plt.figure()
plt.title(title)
ind = np.arange(len(classes))
plt.bar(ind, instances, width=width, align='center')
plt.xticks(range(len(classes)), ['linear', 'gaussian'])
ax = fig2.add_subplot(111)
fig2.subplots_adjust(top=0.85)
ax.set_xlabel('kernel type\n')
ax.set_ylabel('accuracy')
fig2.show()

#wine
title='\nSVM Wine Dataset\n'
print 'Plotting ' + title

classes = [0, 1]
instances = [0.529, 0.451]
width = .35

fig2 = plt.figure()
plt.title(title)
ind = np.arange(len(classes))
plt.bar(ind, instances, width=width, align='center')
plt.xticks(range(len(classes)), ['linear', 'gaussian'])
ax = fig2.add_subplot(111)
fig2.subplots_adjust(top=0.85)
ax.set_xlabel('kernel type\n')
ax.set_ylabel('accuracy')
fig2.show()

raw_input() #keeps plots alive
