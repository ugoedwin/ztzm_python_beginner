items = []

while True:
    print("\n\nWelcome to Minimart!")
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. View cart")
    print("4. Checkout")

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
         print("Invalid choice. Please choose 1, 2, 3, or 4.")

         break