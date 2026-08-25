bills = []
stock = {"pizza": [10, 350], "burger": [10, 220],
         "coffee": [20, 50], "tea": [19, 30], "sandwich": [15, 150], "pasta": [10, 250],
         "fries": [20, 100], "soda": [30, 40], "ice cream": [10, 80], "salad": [15, 120] }


print("\ngrocery billing system.")

while True:
    
    print("1 ________________________________")
    print("choose an option (1-2)?")
    print("1 - Add new bill item; \n2 - Exit")
    choice = int(input("(1, 2): "))

    if choice == 1:
        item_name = input("enter item name: ")

        if item_name not in stock:
            print("The item is currently out of stock.")

            continue

        qty = int(input("enter quantity of item: "))

        if stock[item_name][0] >= qty:
            stock[item_name][0] -= qty

        else:
            print("There isn’t enough of this item currently in stock.")
            continue

        bills.append((item_name, qty, stock[item_name][1]))
        print("Item successfully added to the bill.")

    else:
        print("The bill has been generated and is now being printed.")
        total = 0
        print("Bill:")

        for bill in bills:
            print(str(bill[1]), bill[0], "for",
                  str(bill[1] * bill[2]), "total.")
            total += bill[1] * bill[2]

        print("Total is", str(total))
        break