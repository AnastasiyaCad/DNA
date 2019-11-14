import pickle
import os.path

cpg_island_dict = {}

file = open('annotations.txt', 'r')
line = file.readline()
line_list = line.split('\t')

cpg_key = 'ID_REF'
gene_key = 'UCSC_REFGENE_NAME'
island_key = 'RELATION_TO_UCSC_CPG_ISLAND'
island_id = line_list.index(island_key)
cpg_id = line_list.index(cpg_key)
gene_id = line_list.index(gene_key)

for line in file:
    line_list = line.rstrip().split('\t')

    island_row = line_list[island_id]
    cpg = line_list[cpg_id]

    gene_raw = line_list[gene_id]
    gene_list = gene_raw.split(';')
    gene_list = list(set(gene_list))

    for gene in gene_list:
        if gene != '':
            if island_row == "Island":
                if gene not in cpg_island_dict:
                    cpg_island_dict[gene] = [cpg]
                else:
                    cpg_island_dict[gene].append(cpg)

fname = 'gene_cpg_island_dict.pkl'
with open(fname, 'wb') as handle:
    pickle.dump(cpg_island_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)