result = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        mazrab = str(i * j)
        mazrab_int = int(mazrab)
        if len(mazrab) == 6:
            if mazrab[0] == mazrab[5] and mazrab[1] == mazrab[4] and mazrab[2] == mazrab[3] and result < mazrab_int:
                result = mazrab_int
print(result)
