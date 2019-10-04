#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /mapreduce-test/mapreduce-test-data/access.log /lab_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file Mapper.py -mapper Mapper.py \
-file Reducer.py -reducer Reducer.py \
-input /lab_1/input/* -output /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
../../stop.sh