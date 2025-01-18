# name = "Json"
#
# if len(name) > 50:
#    print("Cannot include more than 50 characters!")
# elif len(name) <3:
#     print("Password must contain at-least 3 characters!")
# else:
#     print("Password looks good!")
#
# for i in range(1, 6):
#     print(i)

students = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob", "scores": [88, 74, 91]},
    {"name": "Charlie", "scores": [95, 89, 85]},
]

for student in students:
    name = student["name"]
    scores = student["scores"]
    average = sum(scores) / len(scores)
    print(f"Student: {name}, Scores: {scores}, Average: {average:.2f}")
