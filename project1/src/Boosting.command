#!/bin/bash

ALGORITHM="ada"
DATASET="wine"
PARAM=10

echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.meta.AdaBoostM1"
rm $FILENAME

for i in `seq 1 $PARAM`;
do
	ITER=$(($i * 20))
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -I $ITER -W weka.classifiers.trees.J48 -- -C 0.25 -M 4)
	echo $ITER
	echo $OUTPUT >> $FILENAME
done

## second dataset
# ALGORITHM="ada"
# DATASET="diabetes"
# PARAM=53
#
# echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"
#
# CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
# FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
# ALGOPATH="weka.classifiers.meta.AdaBoostM1"
# rm $FILENAME
#
# for i in `seq 1 $PARAM`;
# do
# 	ITER=$(($i * 10))
# 	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -I $ITER -W weka.classifiers.trees.J48)
# 	echo $ITER
# 	echo $OUTPUT >> $FILENAME
# done
