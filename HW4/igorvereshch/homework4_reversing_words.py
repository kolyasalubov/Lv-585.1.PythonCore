def reverse(st):
    list_of_words = st.split()
    result = ""
    for i in range(len(list_of_words) - 1,-1,-1):
        result += list_of_words[i] + (" " if i != 0 else "")
    st = result
    return st

print(reverse("Hello World! My name is Igor."))