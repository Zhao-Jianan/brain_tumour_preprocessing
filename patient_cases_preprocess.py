from preprocess_function.batch_preprocessing import preprocess_single_check
from preprocess_function.logger import logger
import os


# ------------------- 核心函数 -------------------
def preprocess_patient_cases_auto(patient_id, input_root_dir, output_root_dir,
                                  reference_mode, model_style, norm_type, plot_mode):
    """
    自动扫描病人文件夹，处理所有条件和时间点
    """
    patient_folder = os.path.join(input_root_dir, patient_id)
    if not os.path.exists(patient_folder):
        logger.error(f"Patient folder not found: {patient_folder}")
        return

    # 获取所有子文件夹
    all_conditions = [
        f for f in os.listdir(patient_folder)
        if os.path.isdir(os.path.join(patient_folder, f))
    ]

    if not all_conditions:
        logger.warning(f"No subfolders found for patient {patient_id}")
        return

    # 按日期排序（假设文件夹名前 8 位是日期）
    all_conditions.sort(key=lambda x: x[:8])

    logger.info(f"{patient_id} - processing {len(all_conditions)} conditions/timepoints: {all_conditions}")

    # 单循环处理
    for condition_name in all_conditions:
        preprocess_single_check(
            input_root_dir,
            output_root_dir,
            patient_id,
            condition_name,
            reference_mode=reference_mode,
            model_style=model_style,
            norm_type=norm_type,
            plot_mode=plot_mode
        )

    logger.info(f"{patient_id} processing complete.")
    logger.info("-"*64)

# ------------------- 批量处理 -------------------
def process_all_patients(input_root_dir, output_root_dir,
                         reference_mode, model_style, norm_type, plot_mode):
    """
    自动扫描 input_root_dir 下所有病人文件夹，批量处理
    """
    patient_ids = [
        f for f in os.listdir(input_root_dir)
        if os.path.isdir(os.path.join(input_root_dir, f))
    ]

    if not patient_ids:
        logger.warning(f"No patient folders found in {input_root_dir}")
        return

    logger.info(f"Found {len(patient_ids)} patients: {patient_ids}")

    for patient_id in sorted(patient_ids):
        preprocess_patient_cases_auto(
            patient_id,
            input_root_dir,
            output_root_dir,
            reference_mode,
            model_style,
            norm_type,
            plot_mode
        )

def main():
    reference_mode="T1ce"
    model_style='nnunet'
    norm_type='std'
    plot_mode='save'

    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed_test/"

    process_all_patients(
        input_root_dir=input_root_dir,
        output_root_dir=output_root_dir,
        reference_mode=reference_mode,
        model_style=model_style,
        norm_type=norm_type,
        plot_mode=plot_mode
    )

    logger.info("All processing complete.")

if __name__ == "__main__":
    main()