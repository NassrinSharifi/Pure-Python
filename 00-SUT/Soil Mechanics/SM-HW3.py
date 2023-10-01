# since we are not given the necessary data ,
# organic soils  and peat are not included in this classification.
def fine_check(PI, a_line_pi):
    str = ""
    if PI < 4 or PI < a_line_pi:
        str = str + "M"
    if PI > 7 or PI >= a_line_pi:
        str = str + "C"
    return str

def w_or_p_gravel(cc, cu):
    str2 = ""
    if cu >= 4 and cc >= 1 and cc <= 3:
        str2 = str2 + "W"
    else:
        str2 = str2 + "P"
    return str2

def w_or_p_sand(cc, cu):
    str2 = ""
    if cu >= 6 and cc >= 1 and cc <= 3:
        str2 = str2 + "W"
    else:
        str2 = str2 + "P"
    return str2

def course_grained(no_4, no_200, PI, LL, cu, cc, a_line_pi, classification_lst=[]):
    gravel = 100 - no_4
    sand = no_4 - no_200
    if gravel > sand:
        classification_lst.append("G")
        if no_200 < 5:
            str2 = w_or_p_gravel(cc, cu)
            classification_lst.append(str2)

        if no_200 >= 5 and no_200 <= 12:
            str2 = w_or_p_gravel(cc, cu)
            classification_lst.append(str2)
            # dual symbols must be used
            classification_lst.append("-G")
            if PI >= a_line_pi:
                classification_lst.append("C")
            else:
                classification_lst.append("M")

        if no_200 > 12:
            str2 = fine_check(PI, a_line_pi)
            classification_lst.append(str2)
        # exception
        if PI >= 4 and PI <= 7 and LL>=12 and LL<=25:
            classification_lst = ["GC-GM"]

    else:
        classification_lst.append("S")
        if no_200 < 5:
            str2 = w_or_p_sand(cc, cu)
            classification_lst.append(str2)

        if no_200 >= 5 and no_200 <= 12:
            str2 = w_or_p_sand(cc, cu)
            classification_lst.append(str2)
            # dual symbols must be used
            classification_lst.append("-S")
            if PI >= a_line_pi:
                classification_lst.append("C")
            else:
                classification_lst.append("M")

        if no_200 > 12:
            str2 = fine_check(PI, a_line_pi)
            classification_lst.append(str2)
        # exception
        if PI >= 4 and PI <= 7 and LL>=12 and LL<=25:
            classification_lst = ["SC-SM"]

    classification_str = ""
    for i in range(len(classification_lst)):
        classification_str = classification_str + classification_lst[i]
    return classification_str

def fine_grained(no_4, no_200, PI, LL, cu, cc, a_line_pi, classification_lst=[]):
    str1 = fine_check(PI, a_line_pi)
    classification_lst.append(str1)
    if LL >= 50:
        classification_lst.append("H")
    else:
        classification_lst.append("L")
        # exception
        if PI >= 4 and PI <= 7 and PI > a_line_pi:
            classification_lst = ["CL-ML"]
    classification_str = ""
    for i in range(len(classification_lst)):
        classification_str = classification_str + classification_lst[i]
    return classification_str

def USCS():
    no_4 = float(input("Enter the percentage passing sieve No.4 :"))
    no_200 = float(input("Enter the percentage passing sieve No.200 :"))
    LL = float(input("Enter the liquid limit of soil :"))
    PI = float(input("Enter the plasticity index of soil :"))
    d10 = float(input("Enter D10:"))
    d30 = float(input("Enter D30:"))
    d60 = float(input("Enter D60:"))
    cu = d60 / d10
    cc = (d30) ** 2 / (d10 * d60)
    a_line_pi = 0.73 * (LL - 20)
    if no_200 < 50:
        soil_class = course_grained(no_4, no_200, PI, LL, cu, cc, a_line_pi, classification_lst=[])
    else:
        soil_class = fine_grained(no_4, no_200, PI, LL, cu, cc, a_line_pi, classification_lst=[])
    return soil_class


# FINAL
print("Please enter only the numbers asked")
soil_class = USCS()
print("According to USCS, the soil sample is classified as :\n " + soil_class)
