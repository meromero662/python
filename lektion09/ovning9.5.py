stack = []

while True:
    print("STACK:")
    for element in stack:
        print("-", element)

    print("\nMENU:")
    print("1. Push")
    print("2. Pop")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        element = input("Enter element to push: ")
        stack.append(element)
        print(f"'{element}' has been pushed onto the stack.")
    elif choice == "2":
        if stack:
            element = stack.pop()
            print(f"'{element}' has been popped from the stack.")
        else:
            print("Stack is empty. Nothing to pop.")
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1 (push), 2 (pop), or 0 (exit).")
