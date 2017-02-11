from matplotlib import pyplot as plt
import numpy as np

#j48 -m 1
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [84.8397, 84.6939, 82.6045, 84.1108, 81.797, 83.3252, 83.3252, 81.8082, 79.9417, 80.7232]
testing_raw = [45.9496, 46.6984, 48.128, 48.6726, 51.8039, 50.9871, 50.9871, 52.0762, 54.8673, 53.4377 ]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Decision Tree Wine Dataset\n'
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

#knn -n 3
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [77.8426, 78.863, 77.0651, 76.8222, 76.7795, 76.2761, 75.8333, 75.8333, 74.5534, 74.4653,74.9198]
testing_raw = [43.5671, 45.405, 48.0599, 49.5575, 49.8298, 50.9871, 53.7781, 53.7781,54.2546,52.4166, 53.3696]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve kNN Wine Dataset\n'
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
training_raw = [62.3907, 62.828,59.378,58.2362,56.126,55.7122, 55.625,  54.9763, 53.9533, 53.3392]
testing_raw = [46.0858,48.4003, 49.8298, 49.081,50.034, 50.7148, 51.3274, 50.919, 50.8509, 50.1021]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve SVM Wine Dataset\n'
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

#boosting adaboostm1 j48 -m 1
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
testing_raw = [47.9238, 50.2383, 51.4636, 51.9401, 56.0926, 58.1348, 59.5643, 60.3131, 61.13, 64.806]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Boosting Wine Dataset\n'
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

#neural net mp 2 epoch
setsize = [10,20,30,40,50,60,70,80,90,100]
training_raw = [57.1429, 52.9155, 50.0486,54.0087, 49.1832, 52.212, 48.625, 53.0806, 52.6248, 51.0353]
testing_raw = [44.3159, 44.3159, 44.5882, 49.3533, 45.7454, 47.4472,45.2008,50.6467,50.1702, 47.8557]

training=[]
testing=[]
for each in range(len(setsize)):
    training.append((float(training_raw[each]) / 100))
    testing.append((float(testing_raw[each]) / 100))

title = '\nLearning Curve Neural Net Wine Dataset\n'
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
