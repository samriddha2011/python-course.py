actual_cost = float(input("Enter the actual cost: "))   
selling_price = float(input("Enter the selling price: "))
if selling_price > actual_cost:
    profit = selling_price - actual_cost
    print("total profit = {0} ".format(profit))
else:
    print("No profit.")