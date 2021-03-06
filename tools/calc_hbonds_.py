#!/usr/bin/python

import MDAnalysis
import MDAnalysis.analysis.hbonds
trjname = ['md100_fit.xtc']
for xtc in trjname:
    outfile = xtc.split('.')[0]+"_hbonds_as_time.cs"
    wf = open(outfile,'w')
    u = MDAnalysis.Universe('begin100.pdb', xtc)
    h = MDAnalysis.analysis.hbonds.HydrogenBondAnalysis(u, 'resname ja2 or protein','resname SOL' distance=3.0, angle=120.0,donors=['1N51','1N12','1N41','1N22','1N31','1N32','1N21','1N42','1N11','1N52','2N31','2N41','2N51','2N11','2N21','3N52','2N52','2N12','3N12','2N22','3N22','3N42','2N42','3N32','2N32','4N32','4N52','4N22','4N12','4N42','N','NE1','1O10','1O20','1O30','1O50','1O40','O42','O21','O52','O11','O32','O31','O51','O12','O41','O22','O','OW'],acceptors=['1N51','1N12','1N41','1N22','1N31','1N32','1N21','1N42','1N11','1N52','2N31','2N41','2N51','2N11','2N21','3N52','2N52','2N12','3N12','2N22','3N22','3N42','2N42','3N32','2N32','4N32','4N52','4N22','4N12','4N42','N','NE1','1O10','1O20','1O30','1O50','1O40','O42','O21','O52','O11','O32','O31','O51','O12','O41','O22','O','OW'])
    h.run()
    h.generate_table()
nt h.table
    for i in range(len(h.table)):
        for j in range(len(h.table[i])):
            wf.write(str(h.table[i][j])+"       ")
        wf.write("\n")
    wf.close()

