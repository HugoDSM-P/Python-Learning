import re

def verify_email(email):
    pattern = r"@\w+\.com"
    verify = re.search(pattern,email)
    if verify:
        print("Ok")
    else:
        print("The email is wrong")

def greetings(phrase):
    pattern = r"^Hello"
    verify = re.search(pattern, phrase)
    if verify:
        print("Ok")
    else:
        print("You didn't greet")

def verify_pc(pc):
    pattern = r"\w{2}\d{4}"
    verify = re.search(pattern,pc)
    if verify:
        print("Ok")
    else:
        print("The postal code is not correct")