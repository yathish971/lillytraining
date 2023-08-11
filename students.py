# Creating a list of student records
students = [
    ["John Doe", 17, 12, ["Math", "Physics", "Chemistry", "English"], "john@example.com", ["Chess", "Debate"]],
    ["Jane Smith", 16, 11, ["Math", "Biology", "English", "History"], "jane@example.com", ["Basketball", "Art Club"]],
    ["Michael Johnson", 15, 10, ["Math", "Geography", "Art", "Spanish"], "michael@example.com", ["Football", "Photography"]],
    ["Emily Brown", 16, 11, ["Physics", "Chemistry", "Biology", "English"], "emily@example.com", ["Swimming", "Gardening"]],
]

# Accessing the first student record
print(students[0])
# Output: ["John Doe", 17, 12, ["Math", "Physics", "Chemistry", "English"]]

# Accessing the third student's name 
print(students[2][0])
# Output: "Michael Johnson"

# Slicing from index 1 to 3 (excluding 3)
print(students[1:3])
# Output:
# [
#   ["Jane Smith", 16, 11, ["Math", "Biology", "English", "History"], "jane@example.com", ["Basketball", "Art Club"]],
#   ["Michael Johnson", 15, 10, ["Math", "Geography", "Art", "Spanish"], "michael@example.com", ["Football", "Photography"]]
# ]

# Slicing from the beginning to index 2 (excluding 2)
print(students[3::])
# Output:
# [
#   ["John Doe", 17, 12, ["Math", "Physics", "Chemistry", "English"], "john@example.com", ["Chess", "Debate"]],
#   ["Jane Smith", 16, 11, ["Math", "Biology", "English", "History"], "jane@example.com", ["Basketball", "Art Club"]]
# ]

# Slicing from index 2 to the end
print(students[2::])
# Output:
# [
#   ["Michael Johnson", 15, 10, ["Math", "Geography", "Art", "Spanish"], "michael@example.com", ["Football", "Photography"]],
#   ["Emily Brown", 16, 11, ["Physics", "Chemistry", "Biology", "English"], "emily@example.com", ["Swimming", "Gardening"]]
# ]

# Accessing the email of the last student 
print("Email id of the Last Student: ",students[-1][4])
# Output: Email of the last student: emily@example.com


