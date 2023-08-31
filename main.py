import csv

file = "Задача на конкурсный отбор.csv"
#массив тех кто не поступит предварительно
questionable = []
last_places = ['', '', '', '', '', '', '', '', '', '']
# вместимость программ
programs_capacity = [40, 40, 90, 80, 40, 40, 50, 40, 30, 40]
current_occupancy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# задаём имена файлам
file = open("Задача на конкурсный отбор.csv", encoding="utf-8")

#чистим файлы
for i in range(1,10):
    name = str(i) + ".csv"
    open(name, 'w').close()


wfiles = [open("1.csv", "r+", encoding="utf-8", newline=''), open("2.csv", "r+", encoding="utf-8", newline=''),
          open("3.csv", "r+", encoding="utf-8", newline=''),
          open("4.csv", "r+", encoding="utf-8", newline=''), open("5.csv", "r+", encoding="utf-8", newline=''),
          open("6.csv", "r+", encoding="utf-8", newline=''), open("7.csv", "r+", encoding="utf-8", newline=''),
          open("8.csv", "r+", encoding="utf-8", newline=''),
          open("9.csv", "r+", encoding="utf-8", newline=''), open("10.csv", "r+", encoding="utf-8", newline='')]

# работа с csv
competitorsDB = csv.reader(file, delimiter=",")

# обработка исходных файлов
for row in competitorsDB:
    priority = int(row[2]) - 1
    extra = int(row[3])-1 if row[3] != '' else -1
    if int(current_occupancy[priority]) < programs_capacity[priority]:
        current_occupancy[priority] += 1
        file_writer = csv.writer(wfiles[priority], delimiter=",")
        file_writer.writerow(row)
        last_places[priority] = row
    elif (row[3] != '') and (int(current_occupancy[extra]) < programs_capacity[extra]):
        current_occupancy[extra] += 1
        file_writer = csv.writer(wfiles[extra], delimiter=",")
        file_writer.writerow(row)
        last_places[extra] = row
    else:
        questionable.append(row)

print(last_places)
#обрабатываем непоступиваших
for data in questionable:
    priority = int(data[2]) - 1
    flag1 = False
    flag2 = False
    dop = "ПОД ВОПРОСОМ НА ПРОГРАММАХ"
    dopNotPassed = "НЕ ПОСТУПИЛ"
    extra = int(data[3]) - 1 if data[3] != '' else -1
    if int(last_places[priority][1]) == int(data[1]):
        dop += " " + data[2]
        flag1 = True
    if int(last_places[extra][1]) == int(data[1]) and (extra != -1):
        flag2 = True
        dop += " и " + data[3]
    if (flag1 == False) and (flag2 == False):
        file_writer1 = csv.writer(wfiles[extra], delimiter = ",")
        file_writer2 = csv.writer(wfiles[priority], delimiter = ",")
        dopNotPassed += "_" + data[2] + "_" + data[3]
        data.append(dopNotPassed)
        file_writer1.writerow(data)
        file_writer2.writerow(data)
    if flag1:
        file_writer = csv.writer(wfiles[priority], delimiter=",")
        data.append(dop)
        file_writer.writerow(data)
    if flag2:
        file_writer = csv.writer(wfiles[extra], delimiter=",")
        data.append(dop)
        file_writer.writerow(data)



#чистим мусор
for file in wfiles:
    file.close()
