items = []

while True:
    print("Welcome to Minimart!")
    option = int((input("Choose an option: ")))

    if option == 1:
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter number of items: "))

        item = {item_name: item_quantity}
        items.append(item)
        print(item_name, "added to cart.")
    elif option == 2:
        item_name = input("Enter item name to remove: ")

        for item in items:
            if item_name in item:
                items.remove(item)
                print(item_name, "removed from cart.")
                break
        else:
            print(item_name, "not found in cart.")

    elif option == 3:
        if not items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            print(items)

    elif option == 4:
        print("\nThank you for shopping! You bought:")
        if len(items) == 0:
            print("Nothing (your cart was empty).")
        else:
            print(items)


    else:
         print("Invalid option. Please choose 1, 2, 3, or 4.")

         break