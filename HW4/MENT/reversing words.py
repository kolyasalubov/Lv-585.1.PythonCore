


def reverse(st):
    st.strip()
    st.replace(" ", "")
    words = st.split()
    reversed_st  = ' '.join(reversed(words))
    return reversed_st