def read_data(filename):
    data = []  # Initialize an empty list
    with open(filename, "r") as file:
        for line in file:
            line = line.strip().split(",")
            data.append(line)
    return data


def print_students(data, class_name):
    count = 0
    print(f"List of students who belong to {class_name}:")
    for row in data:
        if row[2] == class_name:
            count += 1
            print(f"{count}. {row[0]} ({row[1]})")
    if count == 0:
        print("No students found")


filename = input("Enter the name of the text file: ")
data = read_data(filename)
class_name = input("Enter the name of the class: ")
print_students(data, class_name)
