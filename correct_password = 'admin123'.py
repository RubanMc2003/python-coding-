correct_password = "789456"
attempts = 3

while attempts >0:
    password = input("Enter your password:")
    if password == correct_password:
        print('Access Granted')
        break
    attempts -= 1
    print(f'incorrect password:Attempts remainng :{attempts}')
else:
    print("its too many incorrect attempts;Access denied")