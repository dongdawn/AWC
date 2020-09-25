#!/usr/bin/python
import numpy as np 
from MDAnalysis import *
import glob
#trjname = ['md400_fit_dt100.xtc','md100_e400_nr_fit_dt100.xtc']
trjname=glob.glob('*_nopbc_skip10_fit.xtc')

for t in trjname:
    outname = t.split('.')[0]+"_hbondsz_water.cs"
    rf=open(outname,'r')
    wf=open(t.split('.')[0]+'_water-.cs','w')
    for line in rf.readlines():
        col = line.split()
        if (float(col[9]) >=30 and float(col[9]) <=49) or (float(col[10]) >=30 and float(col[10]) <=49):
            wf.write(str(col[7])+"     "+str(col[9])+"    "+str(col[10])+'\n')
    wf.close()
    rf.close()
