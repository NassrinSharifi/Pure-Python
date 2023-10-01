def Group_classification(no_10, no_40, no_200, LL, PI):
    if no_200 <= 35:
        if no_10 <= 50 and no_40 <= 30 and no_200 <= 15 and PI <= 6:
                gc = "A-1-a"
        elif no_40 <=50 and no_200 <=25 and PI <= 6:
                gc = "A-1-b"
        elif no_40 >=51 and no_200 <=10:
            gc = "A-3"
        else:
            if LL <= 40:
                if PI <= 10:
                    gc = "A-2-4"
                if PI >= 11:
                    gc = "A-2-6"
            if LL >= 41:
                if PI <= 10:
                    gc = "A-2-5"
                if PI >= 11:
                    gc = "A-2-7"

    if no_200 >= 36:
        if LL <= 40:
            if PI <= 10:
                gc = "A-4"
            if PI >= 11:
                gc = "A-6"
        if LL >= 41:
            if PI <= 10:
                gc = "A-5"
            if PI >= 11:
                if PI <= (LL - 30):
                    gc = "A-7-5"
                else:
                    gc = "A-7-6"

    return gc


def Group_index(no_200, LL, PI, gc):
    if gc == "A-1-a" or gc == "A-1-b" or gc == "A-3" or gc == "A-2-4" or gc == "A-2-5":
        GI = 0
    elif gc == "A-2-7" or gc == "A-2-6":
        GI = 0.01 * (no_200 - 15) * (PI - 10)
    else:
        GI = (no_200 - 35) * (0.2 + 0.005 * (LL - 40)) + 0.01 * (no_200 - 15) * (PI - 10)

    if GI > 0:
        GI_int = int(GI)
        if GI - GI_int >= 0.5:
            GI = GI_int +1
        else:
            GI = GI_int
    else:
        GI = 0
    return GI


def AASHTO_classification():
    no_10 = float(input("Enter the percentage passing sieve No.10 :"))
    no_40 = float(input("Enter the percentage passing sieve No.40 :"))
    no_200 = float(input("Enter the percentage passing sieve No.200 :"))
    LL = (input("Enter the liquid limit of soil :"))
    PI = (input("Enter the plasticity index of soil :"))
    if LL =="NP" and PI=="":
        soil_class = "A-3(0)"
    else:
        LL=float(LL)
        PI=float(PI)
        gc = Group_classification(no_10, no_40, no_200, LL, PI)
        GI = Group_index(no_200, LL, PI, gc)
        soil_class = gc+"("+str(GI)+")"
    return soil_class




print("Please enter only the numbers asked . ( ex. : 5 --> accepted / 5% --> not accepted )")
soil_class=AASHTO_classification()
print("According to AASHTO Classification System , the soil sample is classified as :\n " +soil_class)