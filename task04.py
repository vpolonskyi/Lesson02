a = input("Введите три числа через запятую: ")
a = a.split(",")
x = float(a[0])
y = float(a[1])
z = float(a[2])

if x+y>z and x+z>y and y+z>x:
    print("Треугольник с сторонами", x, y, z, "существует")
else:
    print("Треугольник с сторонами", x, y, z, "не существует")

print("Сейчас буду сортировать x=" + str(x), "y=" + str(y), "z=" + str(z))
if z < y:
    y, z = z, y
if y < x:
    x, y = y, x
if z < y:
    y, z = z, y
print("Отсортировал x:" + str(x) + " >= y:" + str(y) + " >= z:" + str(z))

a.sort()
x = a.count(a[0])
a.sort(reverse=True)
if x > a.count(a[0]):
    print("В строке найдено", x,"совпадения")
elif x == 1 and a.count(a[0]) == 1:
    print("В строке найдено", 0, "совпадений")
else:
    print("В строке найдено", a.count(a[0]), "совпадения")

