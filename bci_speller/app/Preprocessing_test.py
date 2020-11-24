import numpy as np
import scipy.signal as sp
import scipy.io
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import StandardScaler



path = "C:/Users/user/Documents/BCI_Comp_III_Wads_2004/Subject_A_Test.mat"
sampling_rate = 240
sample_use = math.ceil(0.4*sampling_rate)


data_train = scipy.io.loadmat(path)
raw_data = data_train['Signal']
stimulus = data_train['StimulusCode']
one_exp = len(raw_data[0])
ch_count = len(raw_data[0][0])
raw_data = np.swapaxes(raw_data, 1, 2)

N, w = sp.buttord(0.2, 0.3, 3, 40)
b, a = sp.butter(N, w)
data = sp.filtfilt(b, a, raw_data, axis=2)


data = np.swapaxes(data, 0, 1)
data = np.resize(data, (len(data), len(data[0])*len(data[0][0])))
stimulus = np.resize(stimulus, len(stimulus)*len(stimulus[0]))

rerun = []
true = []
true.append(0)
for i in range(1, len(stimulus)):
    if (stimulus[i]==stimulus[i-1]) or (stimulus[i]==0):
        rerun.append(i)
    else:
        true.append(i)
stimulus = np.delete(stimulus, rerun)

samples = np.zeros((len(keys), ch_count, sample_use))
for i in range(len(keys)):
    for j in range(ch_count):
        samples[i][j] = data[j][true[i]:true[i]+sample_use]
#for model testing use samples[number]
