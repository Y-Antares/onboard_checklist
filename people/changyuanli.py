import numpy as np
import csv
import sys
import os
import matplotlib.pyplot as plt


sample = np.loadtxt('Ag2Se_2ADP50.dat').T

sample_x = sample[0,:]
sample_exp = sample[1,:]
sample_diff = sample[2,:]
sample_cal = sample[3,:]


plt.rc('font',family='Times New Roman')

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


plt.plot(sample_x, sample_exp, 'o', label='Ag2Se', color='b', markerfacecolor='w', markersize=5)

plt.plot(sample_x, sample_cal, '-', label='Calculated Line', color='r', linewidth=2)

plt.plot(sample_x, sample_diff - sample_diff - 1.2, '-', color='black', linewidth=1.5)
plt.plot(sample_x, sample_diff - 1.2, '-', label='Difference', color='g', linewidth=2)

plt.plot(10000, 10000, 'o', label='R$_{w}$ = 0.12364', color='w', markerfacecolor='w', linewidth=0.1)


# plot seeting
plt.title("PDF-Ag2Se_2ADP50", fontsize=16)  
#plt.legend(bbox_to_anchor=(1, 1), loc='upper left', frameon=False, fontsize=10.5)  
plt.legend(frameon=False, fontsize=10.5)  
plt.xlim(1.5, 10)  
plt.ylim(-1.5, 2.3)  
plt.xlabel('r (Å)', fontsize=13)  
plt.ylabel('G (Å$^{-2}$)', fontsize=13)  
plt.tight_layout()  


bwith = 1.5  
ax = plt.gca() 
#ax.spines['top'].set_color('red') 
#ax.spines['right'].set_color('none') 
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.tick_params(width=1, labelsize=11) 


plt.savefig('PDF_Ag2Se_2ADP50', dpi=500)
plt.show()