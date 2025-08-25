from batch_preprocessing import preprocess_single_check

patient_id = "20220705_36034576_PTM"  # 需要处理的病人ID
timepoint = "post_CCRT"  # 需要处理的时间点（例如“术前”）
input_root_dir = "/media/ajhz839/OS/Users/ajhz839/code/Clinical_Data/NIfTI"  # 根文件夹路径
output_root_dir = "/media/ajhz839/OS/Users/ajhz839/code/Clinical_Data/preprocessed"

timepoint_date_map = {
    1: "20220812",
    2: "20221118",
    3: "20230208",
    4: "20230417",
    5: "20230609"
}

condition_names = [
    "20220706_post_OP",
    "20221013_post_CCRT_1_PsPD",
    "20230105_post_CCRT_2"
]

for condition_name in condition_names:
    preprocess_single_check(
        input_root_dir,
        output_root_dir,
        patient_id,
        condition_name,
        reference_mode="T1ce",
        model='nnunet',
        type='no_norm'
    )

# for timepoint_num, date in timepoint_date_map.items():
#     condition_name = f"{date}_{timepoint}_{timepoint_num}"
#     preprocess_single_check(
#         input_root_dir,
#         output_root_dir,
#         patient_id,
#         condition_name,
#         reference_mode="T1ce",
#         model='nnunet',
#         type='no_norm'
#     )