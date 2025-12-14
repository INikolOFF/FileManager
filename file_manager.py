import os

while True:
    print("\n1. Create file")
    print("2. Read file")
    print("3. Delete file")
    print("4. List files")
    print("5. Append to file")   # NEW
    print("6. Exit")             # NEW

    choice = input("Choose an option: ")

    if choice == "1":
        filename = input("File name: ")
        content = input("Content: ")

        with open(filename, "w") as file:
            file.write(content)

        print("File created.")

    elif choice == "2":
        filename = input("File name: ")

        if os.path.exists(filename):
            with open(filename, "r") as file:
                print(file.read())
        else:
            print("File not found.")

    elif choice == "3":
        filename = input("File name: ")

        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted.")
        else:
            print("File not found.")

    elif choice == "4":
        files = os.listdir()

        if not files:
            print("No files found.")
        else:
            for f in files:
                print(f)

    # ===============================
    # NEW APPEND OPTION STARTS HERE
    # ===============================
    elif choice == "5":           # NEW
        filename = input("File name: ")  # NEW

        if os.path.exists(filename):      # NEW
            text = input("Text to append: ")  # NEW
            with open(filename, "a") as file:  # NEW (append mode)
                file.write("\n" + text)   # NEW
            print("Text appended.")       # NEW
        else:
            print("File not found.")      # NEW
    # ===============================
    # NEW APPEND OPTION ENDS HERE
    # ===============================

    elif choice == "6":           # NEW
        print("Goodbye!")
        break

    else:
        print("Invalid option.")