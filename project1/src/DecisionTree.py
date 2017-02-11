# Decision Tree parse output
import matplotlib.pyplot as plt

# dataset 1
algorithm = 'j48'
dataset = 'diabetes'
filename = './output/' + algorithm + '-' + dataset + '.txt'
num = 50  #number of instances
list = [] #str list of correctly classified instance %
validation_errors = [] #float list of %
words = []
error=[]

## parse
with open(filename, "r") as myfile:
	for line in myfile:
		words = line.split()
		i = 0
		for word in words:
			if word == "cross-validation" and (i < len(words) - 7):
				# print words[i+6]
				list.append(words[i + 6])
			if word == "Error" and (i < len(words) - 10):
				# print words[i+9]
				error.append(words[i + 9])
			i = i + 1

for each in list:
	validation_errors.append(1- (float(each) / 100))

training_errors = []
for each in error:
	training_errors.append(1- (float(each) / 100))

levels_base = range(1,num + 1)
levels = []
for each in levels_base:
	levels.append(each * 60)


## stats
print '\nVALIDATION on ' + dataset
print 'lowest error = ' + str(min(validation_errors))
print 'lowest error at pruning level ' + str(validation_errors.index(min(validation_errors)))
print 'highest error = ' + str(max(validation_errors))
print 'highest error at pruning level ' + str(validation_errors.index(max(validation_errors)))
print 'range of errors is ' + str(min(validation_errors)) + ' to ' + str(max(validation_errors))

print '\nTRAINING on ' + dataset
print 'lowest error = ' + str(min(training_errors))
print 'lowest error at pruning level ' + str(training_errors.index(min(training_errors)))
print 'highest error = ' + str(max(training_errors))
print 'highest error at pruning level ' + str(training_errors.index(max(training_errors)))
print 'range of errors is ' + str(min(training_errors)) + ' to ' + str(max(training_errors))

## plot
title = algorithm + ' ' + dataset
print '\nPlotting ' + title
print 'num validation_errors = ' + str(len(validation_errors))
print 'num training_errors = ' + str(len(training_errors))
print 'num of pruning level = ' + str(len(levels))
plot1 = plt.figure(1)
ax = plot1.add_subplot(111)
plot1.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('pruning level')
ax.set_ylabel('error')
plt.plot(levels, validation_errors, linewidth=2.0, label = 'validation error')
plt.plot(levels, training_errors, linewidth=2.0, label = 'training error')
plt.legend()

plt.xlim([min(levels), max(levels)])
plt.ylim(min(validation_errors) - 0.05, max(training_errors) + 0.05)
plt.title('\nDecision Tree Diabetes Dataset\n')
plot1.show()


## dataset 2
algorithm = 'j48'
dataset = 'wine'
filename = './output/' + algorithm + '-' + dataset + '.txt'
num = 50  #number of instances
list = [] #str list of correctly classified instance %
validation_errors = [] #float list of %
words = []
error=[]

## parse
with open(filename, "r") as myfile:
	for line in myfile:
		words = line.split()
		i = 0
		for word in words:
			if word == "cross-validation" and (i < len(words) - 7):
				# print words[i+6]
				list.append(words[i + 6])
			if word == "Error" and (i < len(words) - 10):
				# print words[i+9]
				error.append(words[i + 9])
			i = i + 1

for each in list:
	validation_errors.append(1 - (float(each) / 100))

training_errors = []
for each in error:
	training_errors.append(1 - (float(each) / 100))

levels_base = range(1,num + 1)
levels = []
for each in levels_base:
	levels.append(each * 60)


## stats
print '\nVALIDATION on ' + dataset
print 'lowest error = ' + str(min(validation_errors))
print 'lowest error at pruning level ' + str(validation_errors.index(min(validation_errors)))
print 'highest error = ' + str(max(validation_errors))
print 'highest error at pruning level ' + str(validation_errors.index(max(validation_errors)))
print 'range of errors is ' + str(min(validation_errors)) + ' to ' + str(max(validation_errors))

print '\nTRAINING on ' + dataset
print 'lowest error = ' + str(min(training_errors))
print 'lowest error at pruning level ' + str(training_errors.index(min(training_errors)))
print 'highest error = ' + str(max(training_errors))
print 'highest error at pruning level ' + str(training_errors.index(max(training_errors)))
print 'range of errors is ' + str(min(training_errors)) + ' to ' + str(max(training_errors))

## plot
title = algorithm + ' ' + dataset
print '\nPlotting ' + title
print 'num validation_errors = ' + str(len(validation_errors))
print 'num training_errors = ' + str(len(training_errors))
print 'num of pruning level = ' + str(len(levels))
plot2 = plt.figure(2)
ax = plot2.add_subplot(111)
plot2.subplots_adjust(top=0.85)
ax.set_title('axes title')
ax.set_xlabel('pruning level')
ax.set_ylabel('error')
plt.plot(levels, validation_errors, linewidth=2.0, label = 'validation error')
plt.plot(levels, training_errors, linewidth=2.0, label = 'training error')
plt.legend()

plt.xlim([min(levels), max(levels)])
plt.ylim(min(validation_errors) - 0.05, max(training_errors) + 0.05)
plt.title('\nDecision Tree Wine Datatset\n')
plot2.show()

raw_input() #keeps plots alive
