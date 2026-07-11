def total_clac(bill_amount,tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Total amount to pay: ${total}")

total_clac(150, 20)
