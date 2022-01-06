# Author: MOG 1/6/22

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin" "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for row_number, row in enumerate(rows):
    for name_number, name in enumerate(row):
        student = rows[row_number][name_number]
        if student.lower()[len(student) - 1:] == "s":
            student += "'"
        else:
            student += "'s"
        print(student)

