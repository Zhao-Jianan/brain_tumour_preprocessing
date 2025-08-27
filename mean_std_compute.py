import nibabel as nib
import numpy as np

img = nib.load("20220114_35320313_BSR_20220111_pre_OP_T1.nii.gz")
data = img.get_fdata()

mean_val = np.mean(data)
std_val = np.std(data)

print("Mean:", mean_val, "Std:", std_val)