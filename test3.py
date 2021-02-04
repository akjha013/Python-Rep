# MATH 

import math
# power
# print(2**4)
# x = (2+3)*10-3
# y = 10//3
# print(x)
# x = 45.99
# print(round(x))
# print(math.ceil(x))
# print(math.floor(x))
price = 100000
buyer_hasGoodCredit = False
if buyer_hasGoodCredit:
    print('Buyer has good credit')
    downPayment = 0.1 * price
else:
    print('Buyer has Bad credit')
    downPayment = 0.2 * price
print(f"Down Payment ${downPayment}")

