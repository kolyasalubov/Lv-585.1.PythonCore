string = "python"
  
total_digits = 0
total_letters = 0
  
for s in string:
    if s.isnumeric():
        total_digits += 1
    else:
        total_letters += 1
  
print(f"Total letters found : {total_letters}")
print(f"Total digits found : {total_digits}")