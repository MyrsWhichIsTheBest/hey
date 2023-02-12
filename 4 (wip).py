students = {

}
average_score = 0
while True:
    name = input("name")
    if name.lower() == "x":
        break
    score = int(input("score"))
    students.update({score: name})
for stu in range(len(students)):
    average_score += int(list(students.keys())[stu])
    if int(list(students.keys())[stu]) > int(list(students.keys())[stu - 1]):
        best = int(list(students.keys())[stu])
average_score /= len(students)
best_person = {i for i in students if students[i] == best}
print(f"The Class Average is: {round(average_score)}\n"
      f"Best Student was: {best_person}")
