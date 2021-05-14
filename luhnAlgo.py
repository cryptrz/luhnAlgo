import sys

number = input("Enter your credit card number : ")

def typeCard(num):
    prefix = int(num[0:2])
    prefix2 = int(num[0:1])
    
    if (len(num) == 15 and (prefix == 34 or prefix == 37)):
        return "American Express"
    elif (len(num) == 16 and (prefix >= 51 and prefix <= 55)):
        return "MasterCard"
    elif ((len(num) == 13 or len(num) == 16) and prefix2 == 4):
        return "VISA"
    else:
        return "Invalid"

print("Type : {}".format(typeCard(number)))

if typeCard(number) == "Invalid":
    print("Invalid card number")
    sys.exit()

def calcul1(numCard):
    minusLast = number[0:len(number)-1]
    revertedMinus = minusLast[::-1]
    total1 = []
    for i in range(0, len(revertedMinus), 2):
        temp = ''
        temp = str(int(revertedMinus[i])*2)
        if len(temp) == 2:
            total1.append(temp[0])
            total1.append(temp[1])
        else:
            total1.append(temp)
    return(total1)

def calcul2(numCard):
    total2 = []
    for i in range(1, len(number), 2):
        temp = ''
        temp = str(int(number[i]))
        total2.append(temp)
    return(total2)

def subtotal(result):
    nb = 0
    for i in range(0, len(result)):
        nb = nb + int(result[i])
    return nb

checksum = str(subtotal(calcul1(number)) + subtotal(calcul2(number)))

if checksum[-1] == '0':
    print("This card number is valid")
else:
    print("This card number is NOT valid")