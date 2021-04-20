age = int(input("Enter your age ")) 
def proc_enter_age(age):
    try: 
        if age <= 0: 
            raise ValueError("Age cannot be negative and equal to zero!") 
        elif age % 2 == 0:
            print(f"Age {age} is even")
        else:
            print(f"Age {age} is odd")
    except ValueError as e: 
        print(e) 
print(proc_enter_age(age))