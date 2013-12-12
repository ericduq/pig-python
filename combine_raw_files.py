# This script combines the hourly text files extracted from NLDAS grib files to a panel of data type (e.g., temperature), year, month, day, hour, grid cell number, and value. Each input text file represents a single hourly measure across the grid for ONLY ONE data type.
import sys, string, math, random
import pandas as df
import numpy as np

#info [[line[0:5],line[5:9],line[9:11],line[11:13],line[13:17]] for line in sys.stdin.readlines()]
with open('extracted_files_2days.txt') as f:
	info=[[line[0:5],line[5:9],line[9:11],line[11:13],line[13:17]] for line in f.readlines()]

#print wtype
wtype=info[0][:]
yr=info[1][:]
mo=info[2][:]
day=info[3][:]
hour=info[4][:]
newcolumns=['wtype','yr','mo','day','hour']
test=df.DataFrame(info, columns=newcolumns)
print test
print test.hour
