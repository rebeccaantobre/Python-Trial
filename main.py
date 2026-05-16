print("Hello, Rebecca, your new Python project is set up and ready to go!")
import requests
response = requests.get('https://api.github.com')
print(response.status_code)
name = input("What is your name: ")
print("Nice to meet you, " + name)

age = input("How old are you: ")
if int(age) < 18:
    print("Sorry, you are not old enough to use this program.")
else:
    print("Welcome to the program, " + name + "!")

for i in range(5):
    print("Welcome to the program, Rebecca!")

print("Choose an option:")
print("1. Show your name")
print("2. Show your age")
print("3. Exit")

choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    print("Your name is " + name)
elif choice == "2":
    print("Your age is " + str(age))
else:
    print("Goodbye!")

