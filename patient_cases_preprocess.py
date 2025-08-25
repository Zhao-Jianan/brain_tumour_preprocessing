from preprocess_function.batch_preprocessing import preprocess_single_check


def main():
    reference_mode="T1ce"
    model_style='nnunet'
    norm_type='no_norm'
    plot_mode='save'

    # 20221004_36477104_KHH
    patient_id = "20221004_36477104_KHH"  # 需要处理的病人ID
    timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    condition_names = [
        "20220928_pre_OP",
        "20221005_post_OP",
    ]

    timepoint_date_map = {
        1: "20230111",
        2: "20230331",
        3: "20230629",
        4: "20230918",
        5: "20240112",
        6: "20240317",
        7: "20240422",
        8: "20240607",
        9: "20240725"
    }

    for condition_name in condition_names:
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

    for timepoint_num, date in timepoint_date_map.items():
        condition_name = f"{date}_{timepoint}_{timepoint_num}"
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
    print(f"{patient_id} Processing complete.")
    print("----------------------------------------------------------------")
        
        

    patient_id = "20221107_36656596_KDG"  # 需要处理的病人ID
    timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    condition_names = [
        "20221101_pre_OP",
        "20221108_post_OP",
        "20230117_post_CCRT_1"
    ]

    for condition_name in condition_names:
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
        
    print(f"{patient_id} Processing complete.")
    print("----------------------------------------------------------------")
        
    patient_id = "20220928_21490718_HIG"  # 需要处理的病人ID
    timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    condition_names = [
        "20220901_pre_OP",
        "20221216_post OP&post_CCRT_1_PsPD",
    ]

    timepoint_date_map = {
        2: "20230315",
        3: "20230526",
        4: "20230721"
    }

    for condition_name in condition_names:
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

    for timepoint_num, date in timepoint_date_map.items():
        condition_name = f"{date}_{timepoint}_{timepoint_num}"
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
    print(f"{patient_id} Processing complete.")
    print("----------------------------------------------------------------")    
        
    patient_id = "20220907_36356579_KYG"  # 需要处理的病人ID
    timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    condition_names = [
        "20220828_pre_OP",
        "20220908_post_OP",
        "20221222_post_CCRT_1_PsPD"
    ]

    timepoint_date_map = {
        2: "20230324",
        3: "20230615",
        4: "20230919",
        5: "20231211",
        6: "20240411",
        7: "20240709",
        8: "20241021"
    }

    for condition_name in condition_names:
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

    for timepoint_num, date in timepoint_date_map.items():
        condition_name = f"{date}_{timepoint}_{timepoint_num}"
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
    print(f"{patient_id} Processing complete.")
    print("----------------------------------------------------------------")        
        
    patient_id = "20221130_36656053_KYJ"  # 需要处理的病人ID
    timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    condition_names = [
        "20221117_pre_OP",
        "20221201_post_OP"
    ]

    timepoint_date_map = {
        1: "20230315",
        2: "20230609",
        3: "20230809",
        4: "20230910"
    }

    for condition_name in condition_names:
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

    for timepoint_num, date in timepoint_date_map.items():
        condition_name = f"{date}_{timepoint}_{timepoint_num}"
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
    print(f"{patient_id} Processing complete.")
    print("----------------------------------------------------------------")         
        
        
    print("All processing complete.")
    
if __name__ == "__main__":
    main()