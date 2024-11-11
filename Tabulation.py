def tabulation_output(o,c,cp):
    score = 0
    if cp > o > c:
        cp_percent_o = (cp-o)/o
        o_percent_c = (o-c)/c
        cp_percent_c = cp_percent_o + o_percent_c
        score = cp_percent_c
    elif cp > c and c > o:
        cp_percent_c = (cp-c)/c
        score = cp_percent_c
    else:
        score = 0

    return score
    