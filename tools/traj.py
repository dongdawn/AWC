import os
trjlist=['md100_e100_400nr2.xtc','md100_e400_nr2.xtc','md100_e100_400nr.xtc']
for trj in trjlist:
    oname1=trj.split('.')[0]+'_nopbc_skip10.xtc'
    oname2=trj.split('.')[0]+'_nopbc_skip10_fit.xtc'
    os.system('echo -e "0\n" |gmx trjconv -s md.tpr -f %s -o %s -pbc mol -ur compact -skip 10' %(trj, oname1))
    os.system('echo -e "26\n0\n" |gmx trjconv -f %s -s md.tpr -o %s -fit rot+trans -n index.ndx' %(oname1,oname2))
