# Author: Maaz Sabah Uddin
# StudentId: A00257491
# Assignment 09


# Question 1
print("\n>>>>>>>>>>>>>>>>> QUESTION 01 >>>>>>>>>>>>>>>>>\n")
with open("python_learning.txt", "w") as f:
    f.write("Professor has taught us with full-confidence about this Python course so far.\n")
    f.write("What I have learnt so far is... \n")
    f.write("1- Classes\n")
    f.write("2- Object Creation\n")
    f.write("3- Loops while, for\n")
    f.write("4- Functions arguments, kwargs\n")
    f.write("5- Infinite loop\n")
    f.write("6- Range of loop\n")
    f.write("7- Conditional statements\n")
    f.write("8- Exception handling\n")
    f.write("9- File creation\n")
    f.close()

with open("python_learning.txt", "r") as fR:
    for i in range(3): print(fR.read())
    fR.close()

# Question 2
print("\n>>>>>>>>>>>>>>>>> QUESTION 02 >>>>>>>>>>>>>>>>>\n")
with open("json.json", "w") as fW:
    name = input("Enter your name: ")
    food = input("Enter your favorite food: ")
    counter = 1
    fW.write("users=[\n")
    while name not in ["q", "quit", "Q"]:
        _data = {'name': name, 'food': food}
        fW.write("\t"+str({f"user{str(counter)}": _data})+",\n")
        name = input("\nPress q to quit\nEnter your name: ")
        if name in ["q", "quit", "Q"]:
            break
        food = input("Enter your favorite food: ")
        counter += 1

    fW.write("]")
    fW.close()

with open("json.json", "r") as fR:
    print(fR.read())
    fR.close()

# Question 3
print("\n>>>>>>>>>>>>>>>>> QUESTION 03 >>>>>>>>>>>>>>>>>\n")
with open("age.txt", "w") as fW:
    _fixed = False
    valid = True
    while valid:
        try:
            age = input("Enter your age: ")
            int(age)
        except ValueError as e:
            if age == "five":
                age = 5
                _fixed = True
                valid = False
            print("Invalid age. Please try again!\n")
        else:
            valid = False
            print(f"Your age in dog years is: {int(age)*7}")
            fW.write(str(age) + "\n")
            fW.close()
        finally:
            if _fixed:
                print(f"Your age in dog years is: {int(age) * 7}")
                fW.write(str(age) + "\n")
                fW.close()
