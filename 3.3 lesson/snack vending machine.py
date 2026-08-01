def calculate_change(paid ,price):
    change = paid - price
    return change

snack_price = 25
print("====snack vending machine====")
print("Snack price is:",snack_price)
print("accepted coins are 1,5,10,20\n")

total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("insert a coin(1,5,10,20): "))
    
    if coin!= 1 and coin != 5 and coin != 10 and coin != 20:
        print("Invalid coin, please insert a valid coin.")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Total inserted: {total_inserted}")

    if total_inserted >= snack_price:
        print("enough money inserted.")
        break

    change_due = calculate_change(total_inserted, snack_price)
    print("dispersing snack...")
    
    if change_due == 0:
        pass
    else:
        print(f"dispersing change: {change_due}")
    
print("\n==== PURCHASE SUMMARY ====")
print("snack price:",snack_price)
print("total inserted:",total_inserted)
print("coins inserted:",coins_inserted)
print("change due:",change_due)
print("=================================")
print("Thank you for your purchase!")