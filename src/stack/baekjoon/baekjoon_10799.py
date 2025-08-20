def count_pieces(layout):
    result = 0
    cutting_bars = 0

    i = 0
    while i < len(layout):
        if layout[i] == "(" and layout[i + 1] == "(": # 새로운 쇠막대기 추가
            result += 1
            cutting_bars += 1
        elif layout[i] == "(" and layout[i + 1] == ")": ## 쇠막대기들 자름
            result += cutting_bars
            i += 1 ## 레이저 끝 부분은 넘어감
        else:
            cutting_bars -= 1 ## 잘라진 쇠막대기 제거
        i += 1

    return result