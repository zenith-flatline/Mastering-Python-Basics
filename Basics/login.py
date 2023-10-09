attempts  = 0
attempts_max = 5
def login(name,num):
    user = input("enter your name: ").lower()
    pin = int(input("enter your pin: "))

    if user == name and pin == num:
        return True
    return False
while True:
    if login("neamat",123):
        print("login successful!")
        break
    attempt += 1
    if attempt >+ attempt_max:
        print("login failed")
        break
    print("Either the name or pin not recognized, try again\n:")