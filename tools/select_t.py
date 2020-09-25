rfname='md400_fit_dt100_hbondsz.cs'
rf=open(rfname,'r')
wf=open('triazloe.hb','w')
for line in rf.readlines():
    col = line.split()
    if col[6] in ['1N12','2N12','3N12','1N22','2N22','3N22','1N32','2N32','3N32','1N42','2N42','3N42','1N52','2N52','3N52']:
        wf.write(str(col[7])+"     "+str(col[9])+'\n')
wf.close()
