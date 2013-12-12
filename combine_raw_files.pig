DEFINE test_stream `python combine_raw_files.py` SHIP ('/home/hduser/python/combine_raw_files.py');
A = LOAD 'extracted_files_2days.txt' USING PigStorage(',') AS (filename: chararray);
B = STREAM A THROUGH test_stream;
DUMP B;
