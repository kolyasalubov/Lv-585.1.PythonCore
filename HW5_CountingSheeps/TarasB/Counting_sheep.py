from functools import reduce
array1 = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def counting_sheep(arrayOfsheep): #creating a function
    number_of_sheeps = 0    # seting the counter to zero
    for sheep in arrayOfsheep:  #creating a loop
        if(sheep == True):  #seting the condition of counting
            number_of_sheeps += 1   # adding one to the number
    return number_of_sheeps


# using funtion count

def counting_sheep(arrayOfsheep):
    return arrayOfsheep.count(True)

# list comprehension

def counting_sheep(arrayOfsheep):
    return len([sheep for sheep in arrayOfsheep if sheep])