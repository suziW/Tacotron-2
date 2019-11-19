import numpy as np
import matplotlib.pyplot as plt

audio = np.load('training_data/audio/audio-LJ001-0001.npy')
print('audio:', audio.shape, audio.shape[0]/22050)
linear = np.load('training_data/linear/linear-LJ001-0001.npy')
print('linear:', linear.shape, linear.shape[0]/22050)
mels = np.load('training_data/mels/mel-LJ001-0001.npy')
print('mels:', mels.shape, mels.shape[0]/22050)

plt.figure()
plt.plot(audio)

plt.figure()
plt.pcolormesh(linear.T)

plt.figure()
plt.pcolormesh(mels.T)

plt.show()