a = input("Нужно что-то ввести (по умолчанию - Homework): ")
if a == "":
    a = "Homework"
    print("Ну что ж, пусть будет 'Homework'")

b = a.strip()
b = b.replace(".", "")
c = b.replace("-", "")

if c.isdigit() and b.find("-") == b.rfind("-") and b.find("-") <= 0 and a.find(".") == a.rfind("."):
    print("Ба, да это ж число:", a.strip())
else:
    print(a, "- это не число")

print("В строке пробелов:", len(a) - len(a.replace(" ", "")))
print("В строке точек:", len(a) - len(a.replace(".", "")))

if len(a) < 99:
    print("Строка длинною", len(a.center(100)), "символов +", a.center(100), "+")
    print("Для зануд, на строку ниже - ровно 100 символов:")
    print(a.center(100))
else:
    print("Слишком длинная строка что б 'обложить' пробелами :(")

print("Все с большой буквы:", a.title())
