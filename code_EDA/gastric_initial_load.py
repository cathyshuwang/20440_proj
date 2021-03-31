import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'FC2018_protein_quant.xls'

gastric_df = pd.read_excel(file)

# use first row as heading 
new_header = gastric_df.iloc[0]
# remove first row from dataframe
gastric_df = gastric_df[1:]
# assign as column names
gastric_df.columns = new_header

## cleaning
# manually determine which columns irrelevant, indices to remove
to_del = [0, 1] + list(range(3, 10)) + list(range(34, 109))
# remove raw, un-logged values "Corr"
to_del = to_del + list(range(10,22))
gastric_df = gastric_df.drop([gastric_df.columns[x] for x in to_del],  axis='columns')

# convert X, NaN to 1, 0
gastric_df = gastric_df.fillna(0)
gastric_df = gastric_df.replace(['X'],1)
gene_list = gastric_df.Gene
gastric_df = gastric_df.drop(['Gene'],  axis='columns')
gastric_df.to_csv('clean_gastric.csv')
gastric_df

## aggregating data with representative value
# create averages among samples for preliminary plotting 
col = gastric_df.loc[:, "NC1 Log2":"NC4 Log2"]
gastric_df['avg_NC_log2'] = col.mean(axis=1)

col = gastric_df.loc[:, "GC1 Log2":"GC4 Log2"]
gastric_df['avg_GC_log2'] = col.mean(axis=1)

col = gastric_df.loc[:, "PL1 Log2":"PL4 Log2"]
gastric_df['avg_PL_log2'] = col.mean(axis=1)

# drop redundant, single sample data
avg_gastric_df = gastric_df.drop([gastric_df.columns[x] for x in list(range(0,13))],  axis='columns')
avg_gastric_df.to_csv('avg_gastric.csv')
avg_gastric_df


# plot first 100 proteins
n = 100
xx = list(range(n))

fig = plt.figure(figsize=(15,10))
plt.bar(xx, avg_gastric_df['avg_NC_log2'][0:n], alpha=0.3);
plt.bar(xx, avg_gastric_df['avg_GC_log2'][0:n], alpha=0.3);
plt.bar(xx, avg_gastric_df['avg_PL_log2'][0:n], alpha=0.3);
plt.legend(['NC', 'PL', 'GC'], loc='best');
plt.ylim([12,23]);
plt.xlabel('Protein index')
plt.ylabel('Log2 expression level');
fig.savefig('prelim_gastric.png')