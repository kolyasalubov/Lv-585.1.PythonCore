def greet(name):    
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

for name in ["James", "Jenny", "Johnny", "Jackie", "Javier"]:
    print(f"Greet for {name}: " + greet(name))