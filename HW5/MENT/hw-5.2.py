#Не впевнений що це так мало бути, але код працює
name = input("Enter your name: ")

while True:
    if name == "First":
        print("Hello, ", name)
        break
    else:
        print("Error")
        input("Enter your correct name: ")
