#!/usr/bin/python
import numpy as np 
from MDAnalysis import *
import glob
pdb_name = "begin100.pdb"
#trjname = ['md400_fit_dt100.xtc','md100_e400_nr_fit_dt100.xtc']
trjname=glob.glob('*_nopbc_skip10_fit.xtc')
s = Universe(pdb_name)
def sol_center(g):            #g is the resid of gol
    sel = s.select_atoms("resid %s" %g)
    xyz = sel.center_of_mass()
    return xyz[2]

for t in trjname:
    s.load_new(t)
    fname = t.split('.')[0]+"_water_num.cs"
    wf = open(fname,'w')
    for ts in s.trajectory:
        sol = s.select_atoms('resname SOL and (cyzone 10 25 -16 resname ja2 or protein)')
        for sol_index in sol.residues.resids:
            zz=sol_center(sol_index)
            wf.write(str(zz)+'\n')
    wf.close()
