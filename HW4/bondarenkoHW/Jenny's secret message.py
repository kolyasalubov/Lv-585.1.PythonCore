def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

for name in ["Alex", "Tom", "Johnny", "Jhon", "Slavko"]:
    print(f"Greet for {name}: " + greet(name))