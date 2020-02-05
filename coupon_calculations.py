def calculate_order():
    to = 0
    ic = 0
    pc = 0

    input1 = input("Enter number :")
    to = float(input1)

    input2 = input("Enter cash coupon")
    ic = float(input2)

    input3 = input("Enter percent coupon")
    pc = float(input3)

    global total
    total = 0.0

    global temptotal
    temptotal = 0.0

    total = to - ic

    temptotal = pc / 100


    temptotal = total * temptotal




    total = total - temptotal

    if total < 10.0:
        total = total + 5.95


    elif total >= 10 and total < 30:
        total = total + 7.95


    elif total >= 30 and total <= 50:
        total = total + 11.95

    elif total >= 60:
        total = total + 0


    print(total)
    return total




if __name__ == '__main__':


    calculate_order()

