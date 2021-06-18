#Load up the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from datamatrix import io

#file paths
src = '/Users/keithgraham/Desktop/01. Rotations /Health informatics/IlluminaAudit/MetricsOutput (1).tsv'
src1 = '/Users/keithgraham/Desktop/01. Rotations /Health informatics/IlluminaAudit/MetricsOutputWithRNAMetrics.txt'


#read .tsv file in the directory using pandas
# poke = pd.read_csv('MetricsOutput (1).tsv')

#read .tsv file in src using pandas

# header = pd.read_csv(src, sep='\t', skiprows=3, nrows=3)
# run_QC_Metrics = pd.read_csv(src, sep='\t', skiprows=7, nrows=5)
# analysis_Status = pd.read_csv(src, sep='\t', skiprows=13, nrows=5)
# dNA_Library_QC = pd.read_csv(src, sep='\t', skiprows=19, nrows=4)
# dNA_Library_QC_Metrics_For_Small_Variant_Calling_And_TMB = pd.read_csv(src, sep='\t', skiprows=24, nrows=5)
# dNA_Library_QC_Metrics_For_MSI = pd.read_csv(src, sep='\t', skiprows=30, nrows=3)
# dNA_Library_QC_Metrics_For_CNV = pd.read_csv(src, sep='\t', skiprows=34, nrows=4)
# dNA_Expanded_Metrics = pd.read_csv(src, sep='\t', skiprows=39, nrows=16)
# rNA_Library_QC_Metrics = pd.read_csv(src, sep='\t', skiprows=56, nrows=5)
# rNA_Expanded_Metrics = pd.read_csv(src, sep='\t', skiprows=62, nrows=6)


'''DATA MUNGING USING pd.read_csv()'''

# header = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=3, nrows=3)
# run_QC_Metrics = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=7, nrows=5)
# analysis_Status = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=13, nrows=5)
dNA_Library_QC = pd.read_csv(src, sep='\t', skiprows=21, nrows=3)
# dNA_Library_QC_Metrics_For_Small_Variant_Calling_And_TMB = pd.read_csv('MetricsOutput (1).tsv', sep='\t',
# skiprows=24, nrows=5)
# dNA_Library_QC_Metrics_For_MSI = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=30, nrows=3)
# dNA_Library_QC_Metrics_For_CNV = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=34, nrows=4)
# dNA_Expanded_Metrics = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=39, nrows=16)
# rNA_Library_QC_Metrics = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=56, nrows=5)
# rNA_Expanded_Metrics = pd.read_csv('MetricsOutput (1).tsv', sep='\t', skiprows=62, nrows=6)

'''FIND OUT MORE ABOUT DATAFRAME'''
# print(dNA_Library_QC.columns)
# print(dNA_Library_QC.index)





'''Iteration through row to get axes '''
# y = []
# for col in dNA_Library_QC.columns:
#     if col != 'Metric (UOM)':
#         if col != 'LSL Guideline':
#             y.append(col)

print(dNA_Library_QC.iloc[1])




'''PRINTING DATAFRAMES'''
# print(df.head(5))
# print(df.tail(5))
# print(header)
# print(run_QC_Metrics)
# print(analysis_Status)
# print(dNA_Library_QC)
# print(dNA_Library_QC_Metrics_For_Small_Variant_Calling_And_TMB)
# print(dNA_Library_QC_Metrics_For_MSI)
# print(dNA_Library_QC_Metrics_For_CNV)
# print(dNA_Expanded_Metrics)
# print(rNA_Library_QC_Metrics)
# print(rNA_Expanded_Metrics)

# df = pd.DataFrame(dNA_Library_QC)
'''PRINTING VALUES'''
# print(dNA_Library_QC.loc[1][0])
# print(dNA_Library_QC.iloc[1][3])
# print(dNA_Library_QC.iat[0,0])

'''Intialising the figure and subplot '''
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
# fig, (ax5, ax6, ax7, ax8) = plt.subplots(1,4, figsize=(20,20))

# fig = plt.figure(figsize=(20,10))
# ax1 = fig.add_subplot(421)
# ax2 = fig.add_subplot(422)
# ax3 = fig.add_subplot(423)
# ax4 = fig.add_subplot(424)
# ax5 = fig.add_subplot(425)
# ax6 = fig.add_subplot(426)
# ax7 = fig.add_subplot(427)
# ax8 = fig.add_subplot(428)

# plt.scatter(x,y)
#
# plt.show()

#dNA_Library_QC graph Axes




#yaxis ticks and labels
'''the code below slects row of information from the dataframes create aboce'''
# metric_UOM = dNA_Library_QC.iloc[1]
# print(metric_UOM)
#
# contamination_Scores = dNA_Library_QC.iloc[2]
# print(contamination_Scores)
#
# contamination_P_Values = dNA_Library_QC.iloc[3]
# print(contamination_P_Values)

#learning more about each dataframe
# print(dNA_Library_QC.shape)

##trying to look through to get y_ticks and labels
# yaxis = dNA_Library_QC.iloc[[1]]
# print(yaxis)
# for column in dNA_Library_QC.iloc[[1]]:
#     print(column)




# print(df.iloc[2])

#using datamatix to open .tsv
# dm_csv = io.readtxt('MetricsOutputWithRNAMetrics.txt')
# print(dm_csv)
# print(dm_csv.loc[01-00001])#did not work
# header = pd.read_csv(dm_csv, sep='\t', skiprows=3, nrows=3)
# print(header)

