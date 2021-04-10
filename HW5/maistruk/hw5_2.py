#Write a script that checks the login that the user enters. If the login is "First", then greet the users. If the login is different, send an error message. (need to use loop while)

log = input('Please, enter your login name: ')

while log != "First":
    print ("Your login name was incorrect. \n Please try again.")
    log = input ("Please, eneter your login name: ")
else:
    print (f"You have been succesfully authorized! {log}")
            
