import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy import io

plt.rcParams['figure.figsize'] = [8, 5]  # Bigger images

#ecg_signal = nk.data(dataset="ecg_3000hz")['ECG']

mat_file = io.loadmat('./202m (1).mat').get('val').T
mat_file = np.reshape(mat_file,(mat_file.shape[0],))

ecg_signal = mat_file


# Extract R-peaks locations
_, rpeaks = nk.ecg_peaks(mat_file, sampling_rate=360)


_, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=360, show=False, show_type='peaks')

#waves_peak = waves_peak[~np.isnan(waves_peak)]

plt.plot(ecg_signal)
p1, p2, p3, p4, p5 = 0,0,0,0,0
for i in range(len(waves_peak['ECG_P_Peaks'])):

    try:
        p1=plt.scatter(waves_peak['ECG_P_Peaks'][i],ecg_signal[waves_peak['ECG_P_Peaks'][i]],c='#17becf',label = 'P peaks')
    except:
        None
    try:
        p2=plt.scatter(waves_peak['ECG_Q_Peaks'][i],ecg_signal[waves_peak['ECG_Q_Peaks'][i]],c='#7f7f7f',label = 'Q peaks')
    except:
        None
    try:
        p3=plt.scatter(rpeaks['ECG_R_Peaks'][i],ecg_signal[rpeaks['ECG_R_Peaks']][i],c='#ff0000',label = 'R peaks')
    except:
        None
    try:
        p4=plt.scatter(waves_peak['ECG_S_Peaks'][i],ecg_signal[waves_peak['ECG_S_Peaks'][i]],c='#a22728',label = 'S peaks')
    except:
        None
    try:
        p5=plt.scatter(waves_peak['ECG_T_Peaks'][i],ecg_signal[waves_peak['ECG_T_Peaks'][i]],c='#9467bd',label = 'T peaks')
    except:
        None


'''
plot = nk.events_plot([waves_peak['ECG_T_Peaks'],
                       waves_peak['ECG_P_Peaks'],
                       waves_peak['ECG_Q_Peaks'],
                       waves_peak['ECG_S_Peaks']], ecg_signal,linestyle = 'dotted')
'''
plt.legend((p1,p2,p3,p4,p5),('P peaks','Q peaks','R peaks','S peaks','T peaks'),loc='best')
plt.show()
