import matplotlib.pyplot as plt
import pickle
import os.path

fname = 'gene_cpg_dict.pkl'

with open(fname, 'rb') as handle:
    gene_cpg = pickle.load(handle)

p_age = {}
file = open('observables.txt', 'r')
age_key = 'age'
p_key = 'geo_accession'

line = file.readline().rstrip()
line_list = line.split('\t')
p_id = line_list.index(p_key)
age_id = line_list.index(age_key)
line_age = []
for line in file:
    line_list = line.rstrip().split('\t')

    p = line_list[p_id]
    age = line_list[age_id]
    p_age[p] = age
    line_age.append(int(age))
print(line_age)

file_betas = open('betas.txt', 'r')
line = file_betas.readline()
line_list = line.split('\t')
gene_name = 'FHL2'
#gene_name = 'ELOVL2'
# вводим нужный нам ген

line_cpg = gene_cpg[gene_name]
print(len(line_cpg))
print(line_cpg)
cpg_betas = []
# cpg_id = line_list.index(cpg_key)
for line in file_betas:
    #line = file_betas.readline()
    line = line.replace('\n', '')
    line_list = line.split('\t')
    line_pi = []
    list_cpg = []

    if line_list[0] in line_cpg:
        list_cpg.append(line_list[0])
        print(line_list[0])
        for it in line_list[1:]:
            line_pi.append(float(it))
        cpg_betas.append(line_pi)
        #print(line_pi)

   # print(line_pi)
#print(cpg_betas)
#a = 0

#mpl.plot(line_age, cpg_betas)
#mpl.show()

i = 0
while i < len(cpg_betas):
    plt.scatter(line_age, cpg_betas[i], label='', color='k', s=8)
    plt.title(line_cpg[i])
    plt.xlabel('age')
    plt.ylabel('β')
    plt.show()
    i += 1