def reverse(st):
    reversed_words = st.split()
    result = ""
    for i in range(len(reversed_words) - 1,-1,-1):
        result += reversed_words[i] + (" " if i != 0 else "")
    st = result
    return st

print(reverse("Hi man,how are you doing?"))