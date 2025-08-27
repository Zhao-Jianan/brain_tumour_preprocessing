from preprocess_function.batch_preprocessing import preprocess_single_check


def main():
    reference_mode="T1ce"
    model_style='nnunet'
    norm_type='std'
    plot_mode='save'

    timepoint = "post_CCRT"
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed/"

    #1 20220114_35320313_BSR
    patient_id = "20220114_35320313_BSR"  # 需要处理的病人ID

    condition_names = [
        "20220111_pre_OP",
        "20220115_post_OP",
    ]

    timepoint_date_map = {
        1: "20220414",
        2: "20220706",
        3: "20230907",
        4: "20231101"
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
        
    #2 20220125_35306247_YJS
    patient_id = "20220125_35306247_YJS"  # 需要处理的病人ID

    condition_names = [
        "20220115_pre_OP",
        "20220126_post_OP",
        "20220420_post_CCRT_1_PsPD"
    ]

    timepoint_date_map = {
        2: "20220514",
        3: "20220614",
        4: "20220811",
        5: "20221013",
        6: "20221219",
        7: "20230307",
        8: "20230726",
        9: "20231002",
        10: "20231229",
        11: "20240311",
        12: "20240701",
        13: "20241118",
        14: "20250224"

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

    #3 20220208_34607428_JGT
    patient_id = "20220208_34607428_JGT"  # 需要处理的病人ID

    condition_names = [
        "20220129_pre_OP",
        "20220209_post_OP",
        "20220428_popst_GKS",
        "20220618"
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

    #4 20220428_35588311_MJA
    patient_id = "20220428_35588311_MJA"  # 需要处理的病人ID

    condition_names = [
        "20220411_pre_OP",
        "20220429_post_OP",
        "20221026_post_CCRT_2_PsPD"
    ]

    timepoint_date_map = {
        1: "20220810",
        3: "20230206",
        4: "20230503",
        5: "20230713",
        6: "20231016",
        7: "20240115",
        8: "20240416",
        9: "20240716",
        10: "20241107",
        11: "20250310"
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

    #5 20220510_35765536_PYH
    patient_id = "20220510_35765536_PYH"  # 需要处理的病人ID

    condition_names = [
        "20220502_pre OP",
        "20220511_post OP"
    ]

    timepoint_date_map = {
        1: "20220812",
        2: "20221118",
        3: "20230208",
        4: "20230417",
        5: "20230609"
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

    #6 20220705_36034576_PTM
    patient_id = "20220705_36034576_PTM"  # 需要处理的病人ID

    condition_names = [
        "20220701_pre_OP",
        "20220706_post_OP",
        "20221013_post_CCRT_1_PsPD"
    ]

    timepoint_date_map = {
        2: "20230105"
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

    #7 20220907_36356579_KYG
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

    #8 20220928_21490718_HIG
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

    #9 20221004_36477104_KHH
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
        
        
    #10 20221107_36656596_KDG
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

    #11 20221130_36656053_KYJ   
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