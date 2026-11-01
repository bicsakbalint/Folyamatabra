import random

eletkor = 19
diak = True
if eletkor <= 6:
    print("Ingyenes")
else:
    if eletkor < 18 and diak == True:
        print("Diákjegy: 1800 Ft")
    else:
        if eletkor >= 65:
            print("Nyugdíjas jegy: 2000 Ft")
        else:
            print("Teljesárú jegy: 3000 Ft")
