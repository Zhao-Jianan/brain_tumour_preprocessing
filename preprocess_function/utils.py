


# 筛选函数
def is_target_modality(filename, special_names):
    if special_names == None:
        t1ce_patterns = [
        "T1_AX_Gadovist_1mm",
        "T1_AX_1MM_Gadovist",
        "T1_Gadovist_AX_1MM",
        "T1_AX_Gadovist_1MM",
        ]
        if any(p in filename for p in t1ce_patterns):
            return "T1ce"
        elif "T1_SE_TRA" in filename or 'T1_IR_AX' in filename:
            return "T1"
        elif "T2_TSE_TRA" in filename:
            return "T2"
        elif "FLAIR" in filename:
            return "FLAIR"
        return None 
    else:
        for modality, patterns in special_names.items():
            if any(p in filename for p in patterns):
                return modality
        return None 

# special_names example
#     special_names = {
#     "T1ce": ["T1_AX_Gadovist_1mm", "T1_AX_1MM_Gadovist", "T1_Gadovist_AX_1MM"],
#     "T1": ["T1_SE_TRA", "T1_IR_AX"],
#     "T2": ["T2_TSE_TRA"],
#     "FLAIR": ["FLAIR"]
# }