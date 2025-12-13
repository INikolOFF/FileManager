import os

while True:
    print("\n1. Create file")
    print("2. Read file")
    print("3. Delete file")
    print("4. List files")
    print("5. Exit")

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

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")