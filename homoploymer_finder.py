import sys
import re
import os
import numpy as np

bam = sys.argv[1]
sample = sys.argv[2]
sitefile = sys.argv[3]
prefix = sample+"."+sys.argv[4]

def get_all_match(seq,leftseq,rightseq,site,pos,cigar):
	fre = list(re.finditer(r'(?=({0}))'.format(leftseq),seq))
	beh = list(re.finditer(r'(?=({0}))'.format(rightseq),seq))

	l_min_index = '-'
	r_min_index = '-'
	if beh != []:
		m1 = re.findall(r'^(\d+)S',cigar)
		if m1:
			m1 = int(m1[0])
		else:
			m1 = 0
		beh_list = [i.span()[0] for i in beh]
		r_min_index = np.array(beh_list)[np.abs(np.array(beh_list)+ int(pos)-m1-1-int(site)).argmin()]

	if r_min_index != '-' and fre != []:
		fre_list = [j.span()[0]+len(leftseq) for j in fre if j.span()[0] <= r_min_index]
		if fre_list != []:
			l_min_index = np.array(fre_list)[np.abs(np.array(fre_list)-r_min_index).argmin()]

	return l_min_index, r_min_index

with open(sitefile,"r") as fsite,open(prefix+".homoploymer.repeat.xls","w") as fr,open(prefix+".homoploymer.all.xls","w") as fa:
	fr.write("Sample\tChr\tSite\tRepeat_unit_bases\tLeftseq\tRightseq\tInsert Sequence\tAlt reads\tAll reads\tFreq\n")
	fa.write("Sample\tChr\tSite\tRepeat_unit_bases\tLeftseq\tRightseq\tInsert Sequence\tAlt reads\tAll reads\tFreq\n")
	for line in fsite:
		repeat = []
		repeat_rmdup = []
		alllist = []
		all_rmdup = []
		arr = line.strip().split()
		if line.startswith("染色体"):continue
		if line.startswith("chromosome"):continue
		chr,site,insertseq,leftseq,rightseq = arr
		os.system("samtools view %s %s:%s-%s > %s.sam"%(bam,chr,site,site,sample))#得到某位置的sam
		allcount = os.popen("samtools view %s %s:%s-%s |wc -l"%(bam,chr,site,site)).read().split()[0]#统计某位置read数
		sam1 = sample+".sam"
		with open(sam1,"r") as sam:#读sam
			for line1 in sam:
				arr1 = line1.strip().split()
				sequence = arr1[9]
				l_min_index, r_min_index = get_all_match(sequence,leftseq,rightseq,site,arr1[3],arr1[5])
				if l_min_index != '-' and r_min_index != '-':
					posind = l_min_index
					ainsert = sequence[l_min_index:r_min_index]
					if ainsert == '':
						continue
					alllist.append(ainsert)
					if ainsert in all_rmdup:pass
					else:
						all_rmdup.append(ainsert)
					if len(list(set(ainsert))) == 1:
						if ainsert in insertseq or insertseq in ainsert:
							repeat.append(ainsert)
							if ainsert in repeat_rmdup:pass
							else:
								repeat_rmdup.append(ainsert)

		for i in all_rmdup:
			altcount = alllist.count(i)
			freq = "%.2f"%(float(altcount)/float(allcount)*100)
			fa.write("\t".join([sample,line.strip(),i,str(altcount),str(allcount),freq])+"\n")
		for i in repeat_rmdup:
			altcount = repeat.count(i)
			freq = "%.2f"%(float(altcount)/float(allcount)*100)
			fr.write("\t".join([sample,line.strip(),i,str(altcount),str(allcount),freq])+"\n")
