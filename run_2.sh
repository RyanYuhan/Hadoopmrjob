#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab_1/input/
cp /mapreduce-test/mapreduce-test-data/access.log /mapreduce-test/mapreduce-test-data/access_tem.log
echo -n "Please enter the start time"
read start_time
echo -n "Please enter the end time"
read end_time
echo -e "@@$start_time-$end_time@@" >> /mapreduce-test/mapreduce-test-data/access_tem.log
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /mapreduce-test/mapreduce-test-data/access_tem.log /lab_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /Hadoopmrjob/Mapper_2.py -mapper /Hadoopmrjob/Mapper_2.py \
-file /Hadoopmrjob/Reducer.py -reducer /Hadoopmrjob/Reducer.py \
-input /lab_1/input/* -output /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
rm /mapreduce-test/mapreduce-test-data/access_tem.log
bash /mapreduce-test/stop.sh
