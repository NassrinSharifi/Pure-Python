people=[]
team=0
for i in range(6):
    person=int(input())
    people.append(person)
    if not i%2==0:
        if people[i] < people[i-1]:
            team += people[i]
        else:
            team+=people[i-1]
print(team)

