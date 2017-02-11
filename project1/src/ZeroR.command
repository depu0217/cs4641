#!/bin/bash
ALGORITHM="zeror"
DATASET="wine"
PARAM=1

echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.rules.ZeroR"
rm $FILENAME

for i in `seq 1 $PARAM`;
do
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o)
	echo $i
	echo $OUTPUT >> $FILENAME
done

# ALGORITHM="j48"
# DATASET="nursery"
# PARAM=12960
#
# echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"
#
# CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
# FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
# ALGOPATH="weka.classifiers.trees.J48"
# rm $FILENAME
#
# for i in `seq 1 $PARAM`;
# do
# 	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -M $i)
# 	echo $i
# 	echo $OUTPUT >> $FILENAME
# done
