def task3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekends = int(input("Введите кол-во выходных с Воскресенья: "))
    print("Ваши выходные дни: ", week[:-weekends-1:-1])
    print("Ваши рабочие дни: ", week[:-weekends])


if __name__ == '__main__':
    task3()