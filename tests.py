import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

t = pd.read_csv('table.csv')

# ['Wbgene',
#  'siRNA_prg-1_FC',
#  'siRNA_prg-1_padj',
#  'siR_meg-34_FC',
#  'siR_meg-34_padj']

t.drop('Unnamed: 0', axis=1, inplace=True)
t.rename(columns={'siRNA_prg-1_FC':'prg-1 FC',
 'siRNA_prg-1_padj':'prg-1 sig',
 'siR_meg-34_FC':'meg-34 FC',
 'siR_meg-34_padj':'meg-34 sig'}, inplace=True)

t1 = t.drop(['meg-34 FC','meg-34 sig'], axis=1)
t1['gene']='prg-1'

t2 = t.drop(['prg-1 FC','prg-1 sig'], axis=1)
t2['gene']='meg-34'


fig, axes = plt.subplots(1, 2)

g = sns.swarmplot(ax=axes[0], x='gene', y='prg-1 FC', hue='prg-1 sig', data=t1)
g = sns.swarmplot(ax=axes[1], x='gene', y='meg-34 FC', hue='meg-34 sig', data=t2)

# plt.close(2)
# plt.close(3)
plt.tight_layout()








###
data1 = t.melt(id_vars='Wbgene', value_vars=['siRNA_prg-1_FC','siRNA_prg-1_padj'], var_name='FC', value_name='sig')


#####
# data = t.melt(id_vars='Wbgene', var_name='FC')
# data.set_index('Wbgene', inplace=True)


# value_vars=['siRNA_prg-1_FC','siR_meg-34_FC']