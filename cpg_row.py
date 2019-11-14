import numpy as np
import pickle
import os.path

cpg_row = {}

file_betas = open('betas.txt', 'r')
line = file_betas.readline()
line_list = line.split('\t')

num_cols = len(line_list) - 1 # кол-во столбцов
num_rows = 0 # кол-во строк

for line in file_betas:
    line = line.replace('\n', '')
    line_list = line.split('\t')

    cpg_row[line_list[0]] = num_rows
    num_rows += 1


betas = np.zeros((num_rows, num_cols), dtype=float)
rows = 0

file_betas = open('betas.txt', 'r')
line = file_betas.readline()
line_list = line.split('\t')

for line in file_betas:
    line = line.replace('\n', '')
    line_list = line.split('\t')
    # rows_betas = float(line_list[1::])
    rows_betas = [float(s) for s in line_list[1::]]
    betas[rows, :] = rows_betas
    rows += 1

print(betas)

