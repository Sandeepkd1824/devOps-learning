choice = input("Do you want to read or write to the file? (read/write): ").lower()

if choice == "write":
    text = input("Enter the text you want to write: ")

    file = open("example.txt", "w")  # write mode
    file.write(text)
    file.close()

    print("Content written successfully!")

elif choice == "read":
    try:
        file = open("example.txt", "r")  # read mode
        content = file.read()
        file.close()

        print("File content:")
        print(content)
    except FileNotFoundError:
        print("File not found! Please write something first.")

else:
    print("Invalid choice! Please enter 'read' or 'write'.")
