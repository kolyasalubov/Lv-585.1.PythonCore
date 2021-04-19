def are_you_playing_banjo(name):
    name = list(name)
    if name[0] == "R" or name[0] == "r":
        name.append(" plays banjo")
        name = "".join(name)
        return name
    else:
        name.append(" does not play banjo")
        name = "".join(name)
        return name

 
print(are_you_playing_banjo("Roma"))
