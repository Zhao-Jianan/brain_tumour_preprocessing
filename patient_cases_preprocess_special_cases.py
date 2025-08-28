from preprocess_function.batch_preprocessing import preprocess_single_check
from preprocess_function.logger import logger


def preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                             timepoint_flag, input_root_dir, output_root_dir,
                             patient_id, condition_names, timepoint_date_map, special_names=None):
    """
    处理单个病人的多条件、多时间点影像。
    
    :param reference_mode: str, 参考模态
    :param model_style: str, 模型类型
    :param norm_type: str, 标准化方式
    :param plot_mode: str, 绘图模式
    :param timepoint_flag: str, 时间点标记
    :param input_root_dir: str, 输入路径
    :param output_root_dir: str, 输出路径
    :param patient_id: str, 病人ID
    :param condition_names: list[str], 手动指定的条件名称
    :param timepoint_date_map: dict[int, str], 时间点映射 {timepoint_num: date}
    """
    
    # 处理手动指定条件
    if condition_names:
        for condition_name in condition_names:
            preprocess_single_check(
                input_root_dir,
                output_root_dir,
                patient_id,
                condition_name,
                reference_mode=reference_mode,
                model_style=model_style,
                norm_type=norm_type,
                special_names=special_names,
                plot_mode=plot_mode
            )

    # 处理时间点条件
    if timepoint_date_map:
        for timepoint_num, date in timepoint_date_map.items():
            condition_name = f"{date}_{timepoint_flag}_{timepoint_num}"
            preprocess_single_check(
                input_root_dir,
                output_root_dir,
                patient_id,
                condition_name,
                reference_mode=reference_mode,
                model_style=model_style,
                norm_type=norm_type,
                special_names=special_names,
                plot_mode=plot_mode
            )

    logger.info(f"{patient_id} processing complete.")
    logger.info("-" * 64)



#1 20220114_35320313_BSR
def process_patient_BSR(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
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

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)


#2 20220125_35306247_YJS
def process_patient_YJS(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220125_35306247_YJS"  # 需要处理的病人ID

    condition_names = None

    timepoint_date_map = {
        14: "20250224"
    }
    
    special_names = {
        "T1ce": ["T1_MPRAGE_SAG_FS_256x256_Gadovist_Gr-sp_20250224080604_30001"],
        "T1": ["T1_TSE_IR_TRA"],
        "T2": ["T2_TSE_TRA"],
        "FLAIR": ["FLAIR_SAG_FS_P4_20250224080604_14001"]
    }

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map, special_names)


#3 20220208_34607428_JGT
def process_patient_JGT(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220208_34607428_JGT"  # 需要处理的病人ID

    condition_names = [
        "20220129_pre_OP",
        "20220209_post_OP",
        "20220428_popst_GKS",
        "20220618"
    ]

    timepoint_date_map = None

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)
    

#4 20220428_35588311_MJA
def process_patient_MJA(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
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

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)
    
    
#5 20220510_35765536_PYH
def process_patient_PYH(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220510_35765536_PYH"  # 需要处理的病人ID

    condition_names = [
        "20220502_pre_OP",
        "20220511_post_OP"
    ]

    timepoint_date_map = {
        1: "20220812",
        2: "20221118",
        3: "20230208",
        4: "20230417",
        5: "20230609"
    }

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)


#6 20220705_36034576_PTM
def process_patient_PTM(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220705_36034576_PTM"  # 需要处理的病人ID

    condition_names = [
        "20220701_pre_OP",
        "20220706_post_OP",
        "20221013_post_CCRT_1_PsPD"
    ]

    timepoint_date_map = {
        2: "20230105"
    }

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)


#7 20220907_36356579_KYG
def process_patient_KYG(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220907_36356579_KYG"  # 需要处理的病人ID

    condition_names = None

    timepoint_date_map = {
        7: "20240709",
        8: "20241021"
    }
    
    special_names = {
        "T1ce": ["20240709115233_32001", "20241021113718_31001"],
        "T1": ["T1_TSE_IR_TRA"],
        "T2": ["T2_TSE_TRA"],
        "FLAIR": ["FLAIR_SAG_FS_P4_20240709115233_13001", "FLAIR_SAG_FS_P4_20241021113718_14001"]
    }

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map, special_names)
    

#8 20220928_21490718_HIG
def process_patient_HIG(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20220928_21490718_HIG"  # 需要处理的病人ID

    condition_names = None

    timepoint_date_map = {
        2: "20230315"
    }
    
    special_names = {
        "T1ce": ["20230315160243_28001"],
        "T1": ["T1_TSE_TRA"],
        "T2": ["T2_TSE_TRA"],
        "FLAIR": ["T2_SPC3D_FLAIR_SAG_FS_P4_20230315160243_13001"]
    }    

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map, special_names)
    
    
#9 20221004_36477104_KHH    
def process_patient_KHH(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20221004_36477104_KHH"  # 需要处理的病人ID

    condition_names = None

    timepoint_date_map = {
        9: "20240725"
    }
    
    special_names = {
        "T1ce": ["20240725191159_27001"],
        "T1": ["T1_TSE_IR_TRA"],
        "T2": ["T2_TSE_TRA"],
        "FLAIR": ["T2_SPC3D_FLAIR_SAG_FS_P4_20240725191159_13001"]
    }    

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map, special_names)


#10 20221107_36656596_KDG
def process_patient_KDG(reference_mode, model_style, norm_type, plot_mode, 
                        timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20221107_36656596_KDG"  # 需要处理的病人ID

    condition_names = [
        "20221101_pre_OP",
        "20221108_post_OP",
        "20230117_post_CCRT_1"
    ]
    
    timepoint_date_map = None

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)
    
    
#11 20221130_36656053_KYJ
def process_patient_KYJ(reference_mode, model_style, norm_type, plot_mode, 
                     timepoint_flag, input_root_dir, output_root_dir):
    patient_id = "20221130_36656053_KYJ"  # 需要处理的病人ID

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

    preprocess_patient_cases(reference_mode, model_style, norm_type, plot_mode, 
                                timepoint_flag, input_root_dir, output_root_dir,
                                patient_id, condition_names, timepoint_date_map)



def main():
    reference_mode="T2"
    model_style='nnunet'
    norm_type='std'
    plot_mode='save'

    timepoint_flag = "post_CCRT"
    input_root_dir = "/hpc/ajhz839/data/clinical_data/"  # 根文件夹路径
    output_root_dir = "/hpc/ajhz839/preprocess/preprocessed_special/"


    process_patient_YJS(reference_mode, model_style, norm_type, plot_mode, 
                        timepoint_flag, input_root_dir, output_root_dir)


    #7 20220907_36356579_KYG
    process_patient_KYG(reference_mode, model_style, norm_type, plot_mode, 
                        timepoint_flag, input_root_dir, output_root_dir)

    #8 20220928_21490718_HIG
    process_patient_HIG(reference_mode, model_style, norm_type, plot_mode, 
                        timepoint_flag, input_root_dir, output_root_dir)  

    #9 20221004_36477104_KHH
    process_patient_KHH(reference_mode, model_style, norm_type, plot_mode, 
                         timepoint_flag, input_root_dir, output_root_dir)


    logger.info("All processing complete.")
    
if __name__ == "__main__":
    main()