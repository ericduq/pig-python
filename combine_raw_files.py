# This script combines the hourly text files extracted from NLDAS grib files to a panel of data type (e.g., temperature), year, month, day, hour, grid cell number, and value. Each input text file represents a single hourly measure across the grid for ONLY ONE data type.
import sys, string, math, random
import pandas as df
import numpy as np

#info [[line[0:5],line[5:9],line[9:11],line[11:13],line[13:17]] for line in sys.stdin.readlines()]
with open('extracted_files_2days.txt') as f:
	filenames=[line.strip().strip('\n') for line in f.readlines()] 

units= [[fn[0:5],fn[5:9],fn[9:11],fn[11:13],fn[13:17]] for fn in filenames] 

wtype=units[0][:]
yr=units[1][:]
mo=units[2][:]
day=units[3][:]
hour=units[4][:]
newcolumns=['wtype','yr','mo','day','hour']
units_df=df.DataFrame(units, columns=newcolumns)

filenames= [['../nldas/'+fn] for fn in filenames]

for fn in filenames:
	fn=''.join(fn)
	with open(fn) as f:
		data=[line.strip() for line in f.readlines()]
	print fn
	#print data
