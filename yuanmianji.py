def js_s_xmianji(yuan_xin_jia,r_ban_jin):
##圆心角面积 = 圆心角/360*3.14*圆半径**2
    yuan_mianji =yuan_xin_jia / 360 * 3.14 * r_ban_jin ** 2
    print(f"此扇形面积为:{yuan_mianji}")
    return yuan_mianji
js_s_xmianji(160,30)
