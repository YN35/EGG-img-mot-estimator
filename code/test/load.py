import numpy as np
import pyedflib
import matplotlib.pyplot as plt

import wfdb
import mne

edf = pyedflib.EdfReader("dataset/files/S001/S001R01.edf")

labels = edf.getSignalLabels()
print(labels)

print("Duaration:"+str(edf.getFileDuration()))
print("Freq.:"+str(edf.getSampleFrequencies()))
print("N-Sample(=Freq x Duaration):"+str(edf.getNSamples()))
print("Date:"+str(edf.getStartdatetime()))
print('89317981327321798132',edf.readSignal(0).shape)

plt.plot(edf.readSignal(0),label=labels[0])
plt.plot(edf.readSignal(1),label=labels[1])
plt.plot(edf.readSignal(2),label=labels[2])
plt.legend()
plt.savefig("sin.png")

ann_ref = wfdb.rdann("S001R01",'event',pn_dir="dataset/files/S001")

edf = mne.io.read_raw_edf('dataset/files/S001/S001R01.edf.event')
header = ','.join(edf.ch_names)
np.savetxt('your_csv_file.csv', edf.get_data().T, delimiter=',', header=header)