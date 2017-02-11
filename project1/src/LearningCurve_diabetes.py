from matplotlib import pyplot as plt
import numpy as np

#j48 -m 1
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [90.7407, 87.8505,81.9876, 87.907, 87.3134,75.7764,86.4362, 88.6047,  87.7847,79.1434 ]
testing_raw = [72.7273, 72.2944, 77.9221, 77.0563, 78.355, 75.7764, 74.4589, 74.4589, 77.0563, 77.4892]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Decision Tree Diabetes Dataset\n'
plot1 = plt.figure(1)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_xlabel('training set size')
ax.set_ylabel('accuracy')
plt.plot(setsize, training, linewidth=2.0, label = 'training')
plt.plot(setsize, testing, linewidth=2.0, label = 'testing')
plt.ylim(min(testing) - 0.1, max(training) + 0.1)
plt.legend()
plt.title(title)
plot1.show()

#knn -n 14
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [79.6296, 77.5701, 75.1553, 78.6047, 73.5075, 76.7081, 74.2021, 76.0465, 77.4327, 76.5363]
testing_raw = [65.8009, 66.6667,73.1602,75.3247, 75.3247,76.6234,76.1905, 75.3247, 73.1602, 75.3247]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve kNN Diabetes Dataset\n'
plot1 = plt.figure(2)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_xlabel('training set size')
ax.set_ylabel('accuracy')
plt.plot(setsize, training, linewidth=2.0, label = 'training')
plt.plot(setsize, testing, linewidth=2.0, label = 'testing')
plt.ylim(min(testing) - 0.1, max(training) + 0.1)
plt.legend()
plt.title(title)
plot1.show()

#svm linear
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [79.6296, 78.5047, 78.2609, 78.1395, 76.8657,77.3292, 77.1277, 77.907, 79.089, 76.7225 ]
testing_raw = [65.8009, 65.8009, 74.8918, 77.4892, 77.4892, 79.2208,79.6537, 79.6537,78.7879,79.2208]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve SVM Diabetes Dataset\n'
plot1 = plt.figure(3)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_xlabel('training set size')
ax.set_ylabel('accuracy')
plt.plot(setsize, training, linewidth=2.0, label = 'training')
plt.plot(setsize, testing, linewidth=2.0, label = 'testing')
plt.ylim(min(testing) - 0.1, max(training) + 0.1)
plt.legend()
plt.title(title)
plot1.show()

#boosting adaboostm1 j48 -m 4
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
testing_raw = [76.1905, 69.697, 76.1905, 77.4892, 76.1905, 75.7576, 74.026, 75.3247, 77.0563, 74.8918]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Boosting Diabetes Dataset\n'
plot1 = plt.figure(4)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_xlabel('training set size')
ax.set_ylabel('accuracy')
plt.plot(setsize, training, linewidth=2.0, label = 'training')
plt.plot(setsize, testing, linewidth=2.0, label = 'testing')
plt.ylim(min(testing) - 0.1, max(training) + 0.1)
plt.legend()
plt.title(title)
plot1.show()

#neural net mp 6 epoch
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [79.6296, 78.5047, 72.0497,70.2326, 72.0149, 76.087, 75.7979, 76.5116, 78.6749, 77.2812 ]
testing_raw = [65.8009, 65.8009, 65.8009, 65.8009, 71.4286, 78.355, 78.7879, 77.4892, 79.6537, 78.7879 ]
print len(training_raw)
print len(testing_raw)

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Neural Net Diabetes Dataset\n'
plot1 = plt.figure(5)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_xlabel('training set size')
ax.set_ylabel('accuracy')
plt.plot(setsize, training, linewidth=2.0, label = 'training')
plt.plot(setsize, testing, linewidth=2.0, label = 'testing')
plt.ylim(min(testing) - 0.1, max(training) + 0.1)
plt.legend()
plt.title(title)
plot1.show()


raw_input()
