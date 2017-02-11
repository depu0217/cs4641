# Boosting parse output
from matplotlib import pyplot as plt
import numpy as np

#diabetes
title='\nBoosting Diabetes Dataset\n'
print 'Plotting ' + title

# min num 2
min2_validation = [.690875, .707635, .713222, .718808, .731844, .722533, .724395, .72067]
# min2_training = [.862197, .862197, .862197, .862197, .862197, .862197, .862197, .862197]
num_iter = [10, 20, 30, 40, 50, 60, 70, 100]
 
# min num 3
min3_validation = [.713222, .716946, .726257, .72067, .72067, .72067, .72067, .72067]
# min3_training = [.903166, .903166, 903166, .903166, .903166, .903166, .903166, 903166]

# min num 4
min4_validation = [0.709, .709497, .703911, .711359, .709497, .707635, .707635, .707635]
# min4_training = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# min num 10
min10_validation = [.715084, .715084, .715084, .715084, .715084, .715084, .715084, .715084]
# min10_training = [.959032, .985102, .985102,.985102, .959032, .985102, .985102,.985102]

# min num 24
min24_validation = [.724395, .724395, .724395, .724395, .724395, .724395, .724395, .724395]
# min24_training = [.826816, .826816, .826816, .826816, .826816, .826816, .826816, .826816]


# min num 250

plot1 = plt.figure(1)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('number of iterations')
ax.set_ylabel('accuracy')
plt.plot(num_iter, min2_validation, linewidth=2.0, label = 'min2 validation ')
plt.plot(num_iter, min3_validation, linewidth=2.0, label = 'min3 validation ')
plt.plot(num_iter, min4_validation, linewidth=2.0, label = 'min4 validation ')

plt.ylim(0.675, 0.775)
plt.legend()
plt.title(title)
plot1.show()

#wine
title='\nBoosting Wine Dataset\n'
print 'Plotting ' + title
num_iter = [10, 20, 30, 40, 50, 60, 70, 100]
min1_validation = [.627005, .648294, .649752, .648002, .64946, .649169, .65296, .657918]
min2_validation = [.634879, .639253, .64392, .646836, .656168, .655293, .652377, .65296]
min3_validation = [.62788, .637212, .643045, .647711, .654127, .647711, .654127, .65296]

print len(min1_validation)
print len(min2_training)
print len(num_iter)


plot2 = plt.figure(2)
ax = plot2.add_subplot(111)
plot2.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('number of iterations')
ax.set_ylabel('accuracy')
plt.plot(num_iter, min1_validation, linewidth=2.0, label = 'min1 validation ')
plt.plot(num_iter, min2_validation, linewidth=2.0, label = 'min2 validation ')
plt.plot(num_iter, min3_validation, linewidth=2.0, label = 'min3 validation ')
plt.ylim(0.6, 0.7)
plt.legend()
plt.title(title)
plot2.show()

raw_input() #keeps plots alive
