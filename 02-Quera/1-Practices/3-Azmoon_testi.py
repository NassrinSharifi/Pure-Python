def mark_calculator(sheet, key):  # sheet:lst , key:str
    mark = 0
    for i in range(len(key)):
        test = sheet[i]
        test_key = key[i]
        if test_key == 'A':
            if test[0] == '#':
                test = test[1:]
                if '#' in test:
                    mark -= 1
                else:
                    mark += 3
            elif not '#' in test:
                mark += 0
            else:
                mark -= 1
        if test_key == 'B':
            if test[1] == '#':
                test = test[0:1] + test[2:]
                if '#' in test:
                    mark -= 1
                else:
                    mark += 3
            elif not '#' in test:
                mark += 0
            else:
                mark -= 1
        if test_key == 'C':
            if test[2] == '#':
                test = test[0:2] + test[3:]
                if '#' in test:
                    mark -= 1
                else:
                    mark += 3
            elif not '#' in test:
                mark += 0
            else:
                mark -= 1
        if test_key == 'D':
            if test[3] == '#':
                test = test[0:3]
                if '#' in test:
                    mark -= 1
                else:
                    mark += 3
            elif not '#' in test:
                mark += 0
            else:
                mark -= 1
    return mark

# insert input
n = int(input())
answer_key = input()
k = int(input())
for i in range(1,k+1):
    sheet=[]
    for j in range(1,n+1):
        test = input()
        sheet.append(test)
    # print(sheet)
    mark_of_sheet = mark_calculator(sheet, answer_key)
    print(mark_of_sheet)



