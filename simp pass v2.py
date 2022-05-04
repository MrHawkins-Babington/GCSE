#entering a password

password = "Go123"
username = "Bob"

j=3
for i in range(3):
    if j > 0:
        usr = input("Enter a username :")
        pwd = input("Enter a password :")
        if pwd == password and usr == username:
            print(" Welcome! ")
            break
        else:
            j=j-1
            if j > 0:
                print("Chances left",j)
                print("Incorrect Username or Password try again.")
            else:
                print("Attempt limit reached. Entry denied.")
                break
    else:
        break
    
