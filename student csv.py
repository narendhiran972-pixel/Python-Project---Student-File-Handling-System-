file_path = "records.txt"

def insert_record():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    marks = input("Enter Marks: ")

    with open(file_path, "a") as file:
        file.write(f"{roll}|{name}|{marks}\n")

    print("Record inserted successfully!")

def display_records():
    try:
        with open(file_path, "r") as file:
            print("\n--- All Student Records ---")
            for data in file:
                roll, name, marks = data.strip().split("|")
                print(f"Roll No: {roll} | Name: {name} | Marks: {marks}")
    except FileNotFoundError:
        print("No records found!")

def find_record():
    search_roll = input("Enter Roll Number to find: ")
    flag = False

    try:
        with open(file_path, "r") as file:
            for data in file:
                roll, name, marks = data.strip().split("|")
                if roll == search_roll:
                    print(f"Record Found → {name} scored {marks} marks")
                    flag = True
                    break

        if not flag:
            print("Record does not exist!")

    except FileNotFoundError:
        print("File not available!")

while True:
    print("\n===== MENU =====")
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Find Record")
    print("4. Exit")

    option = input("Choose option: ")

    if option == "1":
        insert_record()
    elif option == "2":
        display_records()
    elif option == "3":
        find_record()
    elif option == "4":
        print("Exiting program...")
        break
    else:
        print("Please enter a valid option!")
