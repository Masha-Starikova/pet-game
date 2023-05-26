n = int(input())
day = input()
weekday = ['Mondey', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day =  weekday.index(day)
a = []
a.append(['..']*day)
b = ['.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9']
c = list(range(10, n+1))
abc = list(a[0]+b+c)
abc = [abc[i:i+7] for i in range(0, len(abc), 7)]
for x in abc:
    print(" ".join(str(k) for k in x))