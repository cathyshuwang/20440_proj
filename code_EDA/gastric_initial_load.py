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

# manually determine which columns irrelevant, indices to remove
to_del = [0, 3, 4, 5, 6, 8, 9] + list(range(34, 109))

gastric_df = gastric_df.drop([gastric_df.columns[x] for x in to_del],  axis='columns')
gastric_df.columns

# need more cleaning here

# plot first 20 proteins for now 
n = 20
xx = list(range(n))

# look at one replicate per disease for now
fig = plt.figure()
plt.bar(xx, gastric_df['NC1 Log2'][0:n], alpha=0.3);
plt.bar(xx, gastric_df['PL1 Log2'][0:n], alpha=0.3);
plt.bar(xx, gastric_df['GC1 Log2'][0:n], alpha=0.3);
plt.legend(['NC', 'PL', 'GC'], loc='best');
plt.ylim([13,22]);
plt.xlabel('Protein index')
plt.ylabel('Log2 expression level');
fig.savefig('prelim_gastric.png')