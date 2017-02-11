#!/bin/bash
ALGORITHM="mp"
DATASET="wine"
PARAM_LOWER=0
PARAM_UPPER=20

echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.functions.MultilayerPerceptron"
rm $FILENAME

for i in `seq $PARAM_LOWER $PARAM_UPPER`;
do
	EPOCH=$(($i * 100))
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -N $EPOCH)
	echo $EPOCH
	echo $OUTPUT >> $FILENAME
done

ALGORITHM="mp"
DATASET="diabetes"
PARAM_LOWER=0
PARAM_UPPER=20

echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.functions.MultilayerPerceptron"
rm $FILENAME

for i in `seq $PARAM_LOWER $PARAM_UPPER`;
do
	EPOCH=$(($i * 100))
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -N $EPOCH)
	echo $EPOCH
	echo $OUTPUT >> $FILENAME
done

# ALGORITHM="mp"
# DATASET="nursery"
# PARAM_LOWER=200
# PARAM_UPPER=600
#
# echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"
#
# CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
# FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
# ALGOPATH="weka.classifiers.functions.MultilayerPerceptron"
# rm $FILENAME
#
# for i in `seq $PARAM_LOWER $PARAM_UPPER`;
# do
# 	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -N $i)
# 	echo $i
# 	echo $OUTPUT >> $FILENAME
# done
