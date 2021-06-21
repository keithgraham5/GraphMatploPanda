'''Prototype using plt.scatter()'''








import pandas as pd
import matplotlib.pyplot as plt


src = '/Users/keithgraham/Desktop/01. Rotations /Health informatics/IlluminaAudit/MetricsOutput (1).tsv'
src1 = '/Users/keithgraham/Desktop/01. Rotations /Health informatics/IlluminaAudit/MetricsOutputWithRNAMetrics.txt'

'''Data Munging'''
dNA_Library_QC = pd.read_csv(src, sep='\t', skiprows=21, nrows=2)
del(dNA_Library_QC['Metric (UOM)'])
del(dNA_Library_QC['LSL Guideline'])

'''Iteration to generate Y axis'''
y = []
for col in dNA_Library_QC.columns:
            y.append(col)
print(y)

'''Iteration to generate the X axis'''
x = []
for i in dNA_Library_QC.iloc[0]:
    x.append(i)
print(x)


'''Generate graph using x,y list iterations'''
plt.scatter(x,y)

'''Graph formatting '''
# plt.title()
# plt.legend()
# plt.xlabel()
# plt.ylabel()

'''Formatting grid of scatter plot '''
plt.grid(color = 'gray', linestyle = '--', alpha = 0.5)



plt.show()