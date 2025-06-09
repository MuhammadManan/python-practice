marks = [23,45,67,89,12,34,56,78,90,100]
# print("Marks:", len(marks))
# print(marks[2:5])
# print(marks[2:5:2])  # Slicing with step
# print(marks[8:2:-1])  # Slicing with negative step

def push(lst, value):
    lst.append(value)

marks.insert(2, 69)
print("Marks after insertion:", marks)
push(marks, 432)
print("Marks after push:", marks)