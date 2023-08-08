import csv

file = "Задача на конкурсный отбор.csv"
#массив тех кто не поступит предварительно
questionable = []
last_places = ['', '', '', '', '', '', '', '', '', '']
# вместимость программ
programs_capacity = [40, 50, 80, 80, 50, 50, 40, 40, 20, 50]
current_occupancy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# задаём имена файлам
file = open("Задача на конкурсный отбор.csv", encoding="utf-8")
wfiles = [open("1.csv", "w", encoding="utf-8", newline=''), open("2.csv", "w", encoding="utf-8", newline=''),
          open("3.csv", "w", encoding="utf-8", newline=''),
          open("4.csv", "w", encoding="utf-8", newline=''), open("5.csv", "w", encoding="utf-8", newline=''),
          open("6.csv", "w", encoding="utf-8", newline=''), open("7.csv", "w", encoding="utf-8", newline=''),
          open("8.csv", "w", encoding="utf-8", newline=''),
          open("9.csv", "w", encoding="utf-8", newline=''), open("10.csv", "w", encoding="utf-8", newline='')]

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
    extra = int(data[3]) - 1 if data[3] != '' else -1
    if int(last_places[priority][1]) == int(data[1]):
        file_writer = csv.writer(wfiles[priority], delimiter=",")
        data.append("ПОД ВОПРОСОМ")
        file_writer.writerow(data)
    elif int(last_places[extra][1]) == int(data[1]) and (extra != -1):
        file_writer = csv.writer(wfiles[extra], delimiter=",")
        data.append("ПОД ВОПРОСОМ")
        file_writer.writerow(data)


#чистим мусор
for file in wfiles:
    file.close()
