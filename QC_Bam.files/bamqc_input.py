import os
import sys 
import re

pipeline_db= 'pipeline.db'

sample_name=[]
path=[]
ab_file=[]

with open(pipeline_db, 'r') as pipeline_db:
    for i in pipeline_db:
        i= i.rstrip().split('\t')
        if re.search(r'GenomeAlignments', i[4]):
            tmp_sample= i[0]
            sample_name.append(tmp_sample)
            tmp_file= i[2]
            ab_file.append(tmp_file)
            tmp_path= i[2].split('/')[:-1]
            tmp_path='/'.join(tmp_path)
            path.append(tmp_path)

#Print output

with open('output.txt', 'w') as output:
    for (s, p, a) in zip(sample_name, path, ab_file):
        output.write("{0}\t{1}\t{2}\n".format(s,p,a))