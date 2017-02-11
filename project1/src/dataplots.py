from matplotlib import pyplot as plt
import numpy as np

#python ~/Desktop/spring2017/cs4641/project1/src/dataplots.py

# first dataset
classes = [0, 1]
instances = [500, 268]
width = .25


fig1 = plt.figure()
title = '\nDiabetes Dataset\n'
print 'Plotting ' + title
plt.title(title)
ind = np.arange(len(classes))
plt.bar(ind, instances, width=width, align='center')
plt.xticks(range(2), ['tested negative', 'tested positive'])
plt.ylim(0, 600)


ax = fig1.add_subplot(111)
fig1.subplots_adjust(top=0.85)
ax.set_xlabel('classes')
ax.set_ylabel('number of isntances')

fig1.show()

# wine
classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
instances_train = [0,0,0,17,109,1015,1547,610,127,4,0]
instaces_test = [0,0,0,3,54,442,651,270,48,1,0]
instances = []
for each in range(11):
    instances.append(instances_train[each] + instaces_test[each])
    print str(instances[each])

width = .35

print len(instances)
print len(classes)

fig2 = plt.figure()
title = '\nWine Dataset\n'
print 'Plotting ' + title
plt.title(title)
ind = np.arange(len(classes))
plt.bar(ind, instances, width=width, align='center')

ax = fig2.add_subplot(111)
fig2.subplots_adjust(top=0.85)
ax.set_xlabel('classes')
ax.set_ylabel('number of isntances')

fig2.show()



raw_input()
