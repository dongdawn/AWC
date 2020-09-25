#!/usr/bin/python
import numpy as np 
from MDAnalysis import * 
import glob
pdb_name = "begin100.pdb"
#trjname = ['md400_fit_dt100.xtc','md100_e400_nr_fit_dt100.xtc']
#trjname=glob.glob('*_nopbc_skip10_fit.xtc')
trjname=glob.glob('md100_e400_nr_nopbc_skip10_fit.xtc')
s = Universe(pdb_name)
def sol_center(g):            #g is the resid of gol
    sel = s.select_atoms("resid %s" %g)
    xyz = sel.center_of_mass()
    return xyz[2]

for t in trjname:
    s.load_new(t)
    fname = t.split('.')[0]+"_hbonds_as_time.cs"
    rf = open(fname,'r')
    outname = t.split('.')[0]+"_hbondsz.cs"
    outname2 = t.split('.')[0]+"_hbonds_zonly.cs"
    wf = open(outname,'w')
    wf2 = open(outname2,'w')
    for line in rf.readlines(): 
        col = line.split()
        time = float(col[0])
        donor_resid = int(col[4])
        acceptor_resid = int(col[7])
        #print int(float(time))
        structure =  s.trajectory[int(time/100)]
        wf.write(str(structure.time)+"     "+col[3]+"     "+col[4]+"     "+col[5]+"     "+col[6]+"     "+col[7]+"     "+col[8]+"    "+col[9]+"    "+col[10])

        if donor_resid >=113:
            wf.write("     "+str(sol_center(donor_resid))+"     ")
            wf2.write(str(sol_center(donor_resid))+"     ")
        else:
            wf.write("      0"+"     ")
            wf2.write("0"+"     ")
        if acceptor_resid >=113:
            wf.write("     "+str(sol_center(acceptor_resid))+"\n")
            wf2.write("     "+str(sol_center(acceptor_resid))+"\n")
        else:
            wf.write("      0"+"\n")
            wf2.write("      0"+"\n")
    rf.close()
    wf.close()
    wf2.close()
    rf=open(outname,'r')
    wf=open(t.split('.')[0]+'_triazloe.cs','w')
    for line in rf.readlines():
        col = line.split()
        if col[6] in ['1N12','2N12','3N12','1N22','2N22','3N22','1N32','2N32','3N32','1N42','2N42','3N42','1N52','2N52','3N52']:
            wf.write(str(col[7])+"     "+str(col[9])+'\n')
    wf.close()
    rf.close()
    rf=open(outname,'r')
    wf=open(t.split('.')[0]+'O1.cs','w')
    for line in rf.readlines():
        col = line.split()
        if col[6] in ['O11','O21','O31','O41','O51']:
            wf.write(str(col[7])+"     "+str(col[9])+'\n')
    wf.close()
    rf.close()
    rf=open(outname,'r')
    wf=open(t.split('.')[0]+'O2.cs','w')
    for line in rf.readlines():
        col = line.split()
        if col[6] in ['O12','O22','O32','O42','O52']:
            wf.write(str(col[7])+"     "+str(col[9])+'\n')
    wf.close()
    rf.close()
