#!/bin/bash
ALGORITHM="smo"
DATASET="wine"
PARAM_LOWER=-2
PARAM_UPPER=2

echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.functions.SMO"
rm $FILENAME

# want powers of 10, for example: 0.01, 0.1, 1, 10, 100
for i in `seq $PARAM_LOWER $PARAM_UPPER`;
do
	CVAL=$(bc -l <<< "10 ^($i)")
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -C $CVAL)
	echo $CVAL
	echo $OUTPUT >> $FILENAME
done

## second datasetALGORITHM="smo"
DATASET="diabetes"
PARAM_LOWER=-2
PARAM_UPPER=2

echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"

CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
ALGOPATH="weka.classifiers.functions.SMO"
rm $FILENAME

# want powers of 10, for example: 0.01, 0.1, 1, 10, 100
for i in `seq $PARAM_LOWER $PARAM_UPPER`;
do
	CVAL=$(bc -l <<< "10 ^($i)")
	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -C $CVAL)
	echo $CVAL
	echo $OUTPUT >> $FILENAME
done

# ALGORITHM="smo"
# DATASET="nursery"
# PARAM_LOWER=-2
# PARAM_UPPER=2
#
# echo "Running $ALGORITHM on $PARAM_LOWER to $PARAM_UPPER instances of the $DATASET dataset"
#
# CLASSPATH=$HOME/Desktop/spring2017/cs4641/project1
# FILENAME=$CLASSPATH/output/$ALGORITHM-$DATASET.txt
# ALGOPATH="weka.classifiers.functions.SMO"
# rm $FILENAME
#
# # want powers of 10, for example: 0.01, 0.1, 1, 10, 100
# for i in `seq $PARAM_LOWER $PARAM_UPPER`;
# do
# 	CVAL=$(bc -l <<< "10 ^($i)")
# 	OUTPUT=$(java -cp $CLASSPATH/weka-3-8-1/weka.jar $ALGOPATH -t $CLASSPATH/data/$DATASET.arff -o -C $CVAL)
# 	echo $CVAL
# 	echo $OUTPUT >> $FILENAME
# done
