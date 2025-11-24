secret_number = 5
attempts = 3
while attempts >0:
    number=int(input("Enter your number:"))
    if number <= 4:
        print("Too low. Try again")
    elif number >= 6:
        print("Too high. Try again")
    elif number >=10:
        print("Your guess is out of range. please guess a number between 1 to 10")
    else:
        print("Congratulations! You guessed the correct number")
for i in range(2,5):
  for j in range(4,10):
    print(f'{i}*{j}={i*j}')

