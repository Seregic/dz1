#задаем коллекцию
a = [2, 5, 8, 11, 14, 18, 21, 25, 30]
#вводим элемент, который будем искать
e = 18
#делаем бинарный поиск
f = 0
l = len(a) - 1
index = -1
while(f<=l) and (index==-1) :
    mid = (f+l)//2
    if a[mid] == e :
       index = mid
    else:
        if e > a[mid]:
            f = mid + 1
        else :
            l = mid - 1
#выводим результат
print(index)