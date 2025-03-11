def recutsion_for_tventythree_task_EGE_2005_oy_to_est_2025_eshkereeeeeee(negr_Alexey, anton):
    if negr_Alexey == anton:return 1
    if negr_Alexey < anton: return 0
    return recutsion_for_tventythree_task_EGE_2005_oy_to_est_2025_eshkereeeeeee(negr_Alexey - 2, anton) + \
        recutsion_for_tventythree_task_EGE_2005_oy_to_est_2025_eshkereeeeeee(negr_Alexey // 2, anton)

print(recutsion_for_tventythree_task_EGE_2005_oy_to_est_2025_eshkereeeeeee(32, 14) * \
      recutsion_for_tventythree_task_EGE_2005_oy_to_est_2025_eshkereeeeeee(14, 1))