import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy as pt
import pickle
import os.path
from plotly import tools
import plotly as py
import plotly.graph_objs as go
import statsmodels.api as sm
import xlrd, xlwt
import openpyxl


with open('list_cpg.pickle', 'rb') as handle:
    line_cpg = pickle.load(handle)

with open('dict_cpg_chr.pickle', 'rb') as handle:
    dict_cpg_chr = pickle.load(handle)

with open('dict_cpg_gene.pickle', 'rb') as handle:
    dict_cpg_gene = pickle.load(handle)

with open('dict_cpg_num.pickle', 'rb') as handle:
    dict_cpg_num = pickle.load(handle)

#with open('matrix_betas.pickle', 'rb') as handle:
#    matrix_betas = pickle.load(handle)

file_betas = open('betas.txt', 'r')
line = file_betas.readline()
line_list = line.split('\t')

num_cols = len(line_list) - 1 # кол-во столбцов
num_rows = len(dict_cpg_num) # кол-во строк

matrix_betas = np.zeros((num_rows, num_cols), dtype=float)
rows = 0

for line in file_betas:
    line = line.replace('\n', '')
    line_list = line.split('\t')
    if line_list[0] in line_cpg:
        rows_betas = [float(s) for s in line_list[1::]]
        matrix_betas[rows, :] = rows_betas
        print(rows)
        rows += 1


a = 0

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

#wb = xlwt.Workbook()
#ws = wb.add_sheet('Table')

wb = openpyxl.load_workbook(filename = 'C:/Users/PC/Documents/Linear_Regression/table.xlsx')
ws = wb['table']

data = ["СpG", "Gene", "Chromosome", "R-squared", "Adj.R-squared", "F-statistic", "Prob(F-statistic)", "Intercept", "Slope"]
i = 1
for x in data:
    ws.cell(row=1, column=i).value = x
    i += 1

k = 2 # по столбцам
j = 0 # по строчкам
i = 0
while i < len(matrix_betas):
    X = sm.add_constant(line_age)
    model = sm.OLS(matrix_betas[i], X)
    results = model.fit()
    #print(model.score(line_age, cpg_betas[i]))
    #print(results.params)
    #rint(results.params[0])
    ws.cell(row=k, column=1).value = line_cpg[i]
    ws.cell(row=k, column=2).value = str(dict_cpg_gene[line_cpg[i]])
    ws.cell(row=k, column=3).value = dict_cpg_chr[line_cpg[i]]
    ws.cell(row=k, column=4).value = results.rsquared
    ws.cell(row=k, column=5).value = results.rsquared_adj
    ws.cell(row=k, column=6).value =results.fvalue
    ws.cell(row=k, column=7).value = results.f_pvalue
    ws.cell(row=k, column=8).value = results.params[0]
    ws.cell(row=k, column=9).value = results.params[1]
    """"
    #ws.write(k, 0, line_cpg[i])
    #ws.write(k, 1, dict_cpg_gene[line_cpg[i]])
    ws.write(k, 2, dict_cpg_chr[line_cpg[i]])
    ws.write(k, 3, results.rsquared)
    ws.write(k, 4, results.rsquared_adj)
    ws.write(k, 5, results.fvalue)
    ws.write(k, 6, results.f_pvalue)
    ws.write(k, 7, results.params[0])
    ws.write(k, 8, results.params[1])
    """
    k += 1
    print(i)
    i += 1
#wb.save('table.xls')
wb.save('C:/Users/PC/Documents/Linear_Regression/table.xlsx')