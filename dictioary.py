import pickle
import os.path

fname = 'gene_cpg_dict.pkl'

if os.path.isfile(fname):
    with open(fname, 'rb') as handle:
        gene_cpg = pickle.load(handle)
else:
    gene_cpg = {}
    file = open('annotations.txt', 'r')

    cpg_key = 'ID_REF'
    gene_key = 'UCSC_REFGENE_NAME'

    line = file.readline().rstrip()
    line_list = line.split('\t')
    cpg_id = line_list.index(cpg_key)
    gene_id = line_list.index(gene_key)

    for line in file:
        line_list = line.rstrip().split('\t')

        cpg = line_list[cpg_id]

        gene_raw = line_list[gene_id]
        gene_list = gene_raw.split(';')
        gene_list = list(set(gene_list))

        for gene in gene_list:
            if gene != '':
                if gene not in gene_cpg:
                    gene_cpg[gene] = [cpg]
                else:
                    gene_cpg[gene].append(cpg)


    with open(fname, 'wb') as handle:
        pickle.dump(gene_cpg, handle, protocol=pickle.HIGHEST_PROTOCOL)

a = 0