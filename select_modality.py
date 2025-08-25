import nibabel as nib
import numpy as np
import os

# 待评估的 T1ce 文件列表
t1ce_files = [
    "20250224_post_CCRT_14_T1_MPRAGE_SAG_FS_256x256_Gadovist_Gr-sp_20250224080604_28001.nii.gz",
    "20250224_post_CCRT_14_T1_MPRAGE_SAG_FS_256x256_Gadovist_Gr-sp_20250224080604_29001.nii.gz",
    "20250224_post_CCRT_14_T1_MPRAGE_SAG_FS_256x256_Gadovist_Gr-sp_20250224080604_30001.nii.gz",
    "20250224_post_CCRT_14_T1_MPRAGE_SAG_FS_256x256_Gadovist_Gr-sp_20250224080604_31001.nii.gz"
]


# ===== 参数设置 =====
t1ce_dir = "/media/ajhz839/OS/Users/ajhz839/code/Clinical_Data/NIfTI/20220125_35306247_YJS/20250224_post_CCRT_14"  # T1ce 文件所在目录
brain_mask_file = None  # 脑掩膜文件，可设置为 None

# ===== 读取脑掩膜 =====
brain_mask = None
if brain_mask_file is not None and os.path.exists(brain_mask_file):
    brain_mask = nib.load(brain_mask_file).get_fdata() > 0

# ===== 获取目录下所有 T1ce 文件 =====
t1ce_files = [f for f in os.listdir(t1ce_dir) if f.endswith(".nii") or f.endswith(".nii.gz")]

# ===== 存储对比度指标 =====
scores = {}

for fname in t1ce_files:
    fpath = os.path.join(t1ce_dir, fname)
    img = nib.load(fpath)
    print("数据 dtype:", img.get_data_dtype())
    print("shape:", img.shape)
    print("header:", img.header)
    
    # 只计算脑区
    if brain_mask is not None:
        img = img[brain_mask]
    
    # 对比度指标
    contrast_std = np.std(img)
    contrast_range = img.max() - img.min()
    
    scores[fname] = {"std": contrast_std, "range": contrast_range}

# ===== 选择最佳文件 =====
best_file = max(scores, key=lambda x: scores[x]["std"])

# ===== 输出结果 =====
print("各文件对比度指标：")
for f, s in scores.items():
    print(f"{f}: std={s['std']:.2f}, range={s['range']:.2f}")

print("\n推荐作为 T1ce 的文件：", os.path.join(t1ce_dir, best_file))
