import os
import matplotlib.pyplot as plt
import numpy as np

def show_slices(data, title=None, cmap='gray', plot_mode='show', save_path=None, save_name=None):
    """
    可视化3个体位平面的切片

    参数：
        data: 3D numpy array
        title: 图像标题
        cmap: 颜色映射
        mode: 'show' 或 'save'
        save_path: 保存目录，mode='save' 时必须提供
        save_name: 保存文件名，mode='save' 时必须提供
    """
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    slices = [data.shape[0]//2, data.shape[1]//2, data.shape[2]//2]
    
    axes[0].imshow(data[slices[0], :, :], cmap=cmap)
    axes[1].imshow(data[:, slices[1], :], cmap=cmap)
    axes[2].imshow(data[:, :, slices[2]], cmap=cmap)
    
    if title:
        fig.suptitle(title)

    if plot_mode == 'show':
        plt.show(block=False)
    elif plot_mode == 'save':
        if save_path is None or save_name is None:
            raise ValueError("Both save_path and save_name must be provided when mode='save'")
        os.makedirs(save_path, exist_ok=True)  # 确保目录存在
        full_path = os.path.join(save_path, save_name)
        plt.savefig(full_path, bbox_inches='tight')
        plt.close(fig)  # 保存后关闭图像，避免占用内存
    else:
        raise ValueError("mode must be 'show' or 'save'")
    
    
# 覆盖图显示函数
def show_overlay(image, mask, title="Overlay"):
    """显示图像和掩模的覆盖图"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 自动选择有脑组织的切片
    slice_x = np.where(mask.sum(axis=(1,2)) > mask.max()*10)[0].mean().astype(int)
    slice_y = np.where(mask.sum(axis=(0,2)) > mask.max()*10)[0].mean().astype(int)
    slice_z = np.where(mask.sum(axis=(0,1)) > mask.max()*10)[0].mean().astype(int)
    
    slices = [slice_x, slice_y, slice_z]
    planes = ['Axial', 'Coronal', 'Sagittal']
    
    for i, (sl, plane) in enumerate(zip(slices, planes)):
        if i == 0:
            img_slice = image[sl, :, :]
            mask_slice = mask[sl, :, :]
        elif i == 1:
            img_slice = image[:, sl, :]
            mask_slice = mask[:, sl, :]
        else:
            img_slice = image[:, :, sl]
            mask_slice = mask[:, :, sl]
        
        axes[i].imshow(img_slice, cmap='gray')
        axes[i].imshow(mask_slice, cmap='jet', alpha=0.3)
        axes[i].set_title(f"{plane} View") 
        axes[i].axis('off')
    
    fig.suptitle(title, y=1.05)
    plt.tight_layout()
    plt.show(block=False)