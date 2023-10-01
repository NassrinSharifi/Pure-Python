Gunnar_input = list(map(int, input().split()))
Emma_input = list(map(int, input().split()))
gunnar_dice1 = [x for x in range(Gunnar_input[0], Gunnar_input[1] + 1)]
gunnar_dice2 = [x for x in range(Gunnar_input[2], Gunnar_input[3] + 1)]
emma_dice1 = [x for x in range(Emma_input[0], Emma_input[1] + 1)]
emma_dice2 = [x for x in range(Emma_input[2], Emma_input[3] + 1)]
gunnar_sums = set()
for dice1 in gunnar_dice1:
    for dice2 in gunnar_dice2:
        gunnar_sums.add(dice1 + dice2)
emma_sums = set()
for dice1 in emma_dice1:
    for dice2 in emma_dice2:
        emma_sums.add(dice1 + dice2)
gunnar_score = 0
emma_score = 0
for g_mark in gunnar_sums:
    for e_mark in emma_sums:
        if g_mark > e_mark:
            gunnar_score += 1
        elif e_mark > g_mark:
            emma_score += 1
if gunnar_score > emma_score:
    print('Gunnar')
elif emma_score > gunnar_score:
    print('Emma')
else:
    print('Tie')

