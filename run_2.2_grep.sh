
#!/bin/sh
bash /mapreduce-test/start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /lab_1/input/
echo -e "Please enter the word you want to count\n"
read word
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal /mapreduce-test/mapreduce-test-data/access_tem.log /lab_1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file /Hadoopmrjob/Mapper_2.2_grep.py -mapper "/Hadoopmrjob/Mapper_2.2_grep.py $word" \
-file /Hadoopmrjob/Reducer_2.2_grep.py -reducer /Hadoopmrjob/Reducer_2.2_grep.py \
-input /lab_1/input/* -output /lab_1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /lab_1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /lab_1/output/
bash /mapreduce-test/stop.sh
