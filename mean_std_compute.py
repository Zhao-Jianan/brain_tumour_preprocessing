import nibabel as nib
import numpy as np

# 读取图像
img = nib.load(r"masked_20220114_35320313_BSR_20220111_pre_OP_0003.nii.gz")
data = img.get_fdata()

# 创建非零掩模
mask = data != 0

# 只对非零像素计算均值和标准差
mean_val = data[mask].mean()
std_val = data[mask].std()

print("Mean (nonzero):", mean_val, "Std (nonzero):", std_val)
