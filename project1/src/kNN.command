#!/bin/bash
ALGORITHM="ibk"
DATASET="wine"
PARAM=50

echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.lazy.IBk"
rm $FILENAME

for i in `seq 1 $PARAM`;
do
	NEIGH=$(($i * 60))
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -K $NEIGH)
	echo $NEIGH
	echo $OUTPUT >> $FILENAME
done

## second dataset
ALGORITHM="ibk"
DATASET="diabetes"
PARAM=50

echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.lazy.IBk"
rm $FILENAME

for i in `seq 1 $PARAM`;
do
	NEIGH=$(($i * 10))
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -K $NEIGH)
	echo $NEIGH
	echo $OUTPUT >> $FILENAME
done

# ALGORITHM="ibk"
# DATASET="nursery"
# PARAM=12960
#
# echo "Running $ALGORITHM on $PARAM instances of the $DATASET dataset"
#
# CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
# FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
# ALGOPATH="weka.classifiers.lazy.IBk"
# rm $FILENAME
#
# for i in `seq 1 $PARAM`;
# do
# 	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -K $i)
# 	echo $i
# 	echo $OUTPUT >> $FILENAME
# done
