def filter_words(st):
    st = st.lower()
    temp = st[0]
    st = st[1:]
    return ' '.join(str(temp.upper() + st).split())