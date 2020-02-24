"""Examples illustrating the use of plt.subplots().
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as io
import os

A = io.loadmat('interp_resultBtoA_random.mat', squeeze_me=True)

original = A["original"]
result = A["result"]
masked = A["masked"]


original = np.array(original[:, :, 0])
result = np.array(result[:, :, 0])
masked = np.array(masked[:, :, 0])


frequency = 10.
sampling_rate = 5
sampling_scheme='periodic'


vr = np.amax(np.absolute(original))



mask = np.zeros(masked.shape)
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if masked[i, j] != 0.:
            mask[i, j] = 1.


result = mask*masked + (1-mask)*result

diff = original - result
diff = np.array(diff)

Rec_SNR = -20.0* np.log(np.linalg.norm(diff)/np.linalg.norm(original))/np.log(10.0)
print(Rec_SNR)


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 6}
import matplotlib
matplotlib.rc('font', **font)

#####################################################################################################
plt.figure()
im = plt.imshow((original), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
plt.title('True frequency slice - ' +str(frequency) + ' Hz', fontweight='bold', fontsize=8)
plt.xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
plt.ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)
plt.colorbar(im,fraction=0.044, pad=0.06)
plt.savefig('/data/GAN-LocalSolver/results/figs/True-' +str(frequency) + 'Hz-' + str(sampling_rate) + '-' + sampling_scheme + '.eps', format='eps', bbox_inches='tight', dpi=200)

plt.figure()
im = plt.imshow((result), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
plt.title(("Reconstruction - SNR: %4.4f dB" % (Rec_SNR)), fontweight='bold', fontsize=8)
plt.xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
plt.ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)
plt.colorbar(im,fraction=0.044, pad=0.06)
plt.savefig('/data/GAN-LocalSolver/results/figs/Interpolation-' +str(frequency) + 'Hz-' + str(sampling_rate) + '-' + sampling_scheme + '.eps', format='eps', bbox_inches='tight', dpi=200)

plt.figure()
im = plt.imshow((masked), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
plt.title('Partial measurements (' + str(sampling_rate) + '% sampling)', fontweight='bold', fontsize=8)
plt.xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
plt.ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)
plt.colorbar(im,fraction=0.044, pad=0.06)
plt.savefig('/data/GAN-LocalSolver/results/figs/Subsampled-' +str(frequency) + 'Hz-' + str(sampling_rate) + '-' + sampling_scheme + '.eps', format='eps', bbox_inches='tight', dpi=200)

plt.figure()
im = plt.imshow((original-result), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
# axarr[1, 1].imshow(original*2 - result*2, vmin=-vr, vmax=vr, cmap="seismic")
plt.title('Reconstruction error x 5', fontweight='bold', fontsize=8)
plt.xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
plt.ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)
plt.colorbar(im,fraction=0.044, pad=0.06)
plt.savefig('/data/GAN-LocalSolver/results/figs/Error-' +str(frequency) + 'Hz-' + str(sampling_rate) + '-' + sampling_scheme + '.eps', format='eps', bbox_inches='tight', dpi=200)

# plt.show()






# f, axarr = plt.subplots(2, 2)
# org = axarr[0, 0].imshow((original), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
# axarr[0, 0].set_title('True frequency slice - ' +str(frequency) + ' Hz', fontweight='bold', fontsize=8)
# axarr[0, 0].set_xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
# axarr[0, 0].set_ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)

# axarr[0, 1].imshow((result), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
# axarr[0, 1].set_title(("Reconstruction - SNR: %4.4f dB" % (Rec_SNR)), fontweight='bold', fontsize=8)
# axarr[0, 1].set_xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
# axarr[0, 1].set_ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)

# axarr[1, 0].imshow((masked), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
# axarr[1, 0].set_title('Partial measurements (' + str(sampling_rate) + '% sampling)', fontweight='bold', fontsize=8)
# axarr[1, 0].set_xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
# axarr[1, 0].set_ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)

# axarr[1, 1].imshow((original-result), vmin=-150., vmax=150., cmap="seismic", aspect='1', extent=[0,50*101,50*101,0])
# # axarr[1, 1].imshow(original*2 - result*2, vmin=-vr, vmax=vr, cmap="seismic")
# axarr[1, 1].set_title('Reconstruction error x 5', fontweight='bold', fontsize=8)
# axarr[1, 1].set_xlabel('In-line direction (m)', fontweight='bold', fontsize=6)
# axarr[1, 1].set_ylabel('Cross-line direction (m)', fontweight='bold', fontsize=6)
# # axarr[1, 1].set_rc('font', weight='bold')
# # f.tight_layout()
# f.subplots_adjust(wspace=.4, hspace=.4)
# f.colorbar(org,fraction=0.044, pad=0.06, ax=axarr.ravel().tolist())
# plt.savefig('/data/GAN-LocalSolver/results/figs/Interpolation-' +str(frequency) + 'Hz-' + str(sampling_rate) + '.png', format='png', bbox_inches='tight', dpi=200)
