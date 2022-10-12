
import math
import numpy as np
import pydicom as pdcm
from annotation import Annotation
from matplotlib import pyplot as plt

XML_PATH = "path to XML folder here"
DCM_PATH = "path to DICOM folder here"
img_name = "20586908"



dcm = pdcm.dcmread(DCM_PATH + img_name + '.dcm')
img = dcm.pixel_array
print(img.shape)
a   = Annotation(XML_PATH, img_name, img.shape)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)
fig.set_figheight(6)
fig.set_figwidth(20)
fig.suptitle('INBreast XML parser')

ax1.imshow(img, cmap='gray')
ax1.set_title('Original DICOM image')
ax2.imshow(a.mask[:,:,0], cmap='gray', alpha=0.5)
ax2.set_title('Tumors contours')
ax3.imshow(a.mask[:,:,1], cmap='gray', alpha=0.5)
ax3.set_title('Calcifications contours')
ax4.imshow(a.mask[:,:,2], cmap='gray', alpha=0.5)
ax4.set_title('Other contours')
plt.show()
