# WHILE LOOP IN PYTHON
# i =1;
# while i<=5:
#     print(i*'B')
#     i+=1

# number guessing game
i = 1
secret = 10
flag = True
while i <= 3 and flag is True:
    guess = int(input('guess : '))
    if guess == secret:
        print('you win')
        flag = False
    i += 1
if flag is True:
    print('you lose')
