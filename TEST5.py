# ROUNDING OFF
weight = input('weight : ')
choice = input("(L)bs or (K)g :").lower()
if choice == 'l' :
    kgWeight = int(weight) * 0.453592
    print(f"Your weight is : {round(kgWeight)} kg")
elif choice == 'k':
    pWeight = int(weight) * 2.20462
    print(f"Your weight is : {round(pWeight)} lbs")
else:
    print('invalid choice')