my_dict = {
    8: "Дракон",
    9: "Змея",
    10: "Лошадь",
    11: "Овца",
    0: "Обезьяна",
    1: "Петух",
    2: "Собака",
    3: "Свинья",
    4: "Крыса",
    5: "Бык",
    6: "Тигр",
    7: "Заяц",
}

k = int(input())
print(my_dict[k % 12])