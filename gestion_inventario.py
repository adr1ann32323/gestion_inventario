from datetime import datetime
#------------------------------------------------------------------------------------
def validate_Product():#
    while True:
        product = input("Enter the product identifier number (only positive numbers, not starting with 0, at least 3 digits, or type 'cancel' to cancel): ").strip()

        if product == "cancel":
            print("\033[91mProcess canceled\033[0m")
            break
        elif not product.isdigit():
            print("Error: The identifier must contain only numbers.")
        elif product.startswith('0'):
            print("Error: The identifier must not start with 0.")
        elif len(product) < 3:
            print("Error: The identifier must have at least 3 digits.")
        else:
            return product
#------------------------------------------------------------------------------------
"""Validates that the entered identifier meets the minimum requirements (positive numbers, no leading zeros, at least 3 digits, no characters)."""
def register(inventory,product_Identifier):
    author = input("Enter author: ").strip().lower()
    product_name = input("Enter product name: ").strip().lower()
    category= input("Enter category: ").strip().lower()

    while not author or not product_name or not category:
        print("Fields cannot be empty.")
        author = input("Enter author: ").strip().lower()
        product_name = input("Enter product name: ").strip().lower()
        category= input("Enter category").strip().lower()
    while True:
        try:
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            if price <=0 or stock <=0:
                print("Invalid values. They cannot be negative and the quantity must be a positive integer.")
            else:
                inventory[product_Identifier] = {
                    "product": product_name,
                    "author": author,
                    "category": category,
                    "price": price,
                    "stock": stock }
                print("\n\033[92mProcess completed successfully.\033[0m")
                break
        except ValueError:
            print("Invalid data. Fields cannot be empty and quantity must be a positive integer.")

#------------------------------------------------------------------------------------
"""Validates that the product is in the inventory and if so, displays all its data"""
def show_products(inventory,consult_product):
    if not consult_product in inventory:
        print("\033[91mThe product is not registered.\033[0m")
    else:
        total= inventory[consult_product]['price'] * inventory[consult_product]['stock']
        print(f"\nId: {consult_product} | "
            f"Author: {inventory[consult_product]['author']} | "
            f"Product: {inventory[consult_product]['product']} | "
            f"Category: {inventory[consult_product]['category']} | "
            f"Price: {inventory[consult_product]['price']} | "
            f"Stock: {inventory[consult_product]['stock']}")

        print(f'Total value in the products: {total:.2f}')
#------------------------------------------------------------------------------------
"""Validates that the product is in the inventory and if so, calls the 'register()' function to update"""
def update_Products(inventory,update_product):
    if not update_product in inventory:
        print("\033[91mThe product is not registered.\033[0m")
    else:
        register(inventory,update_product)
#------------------------------------------------------------------------------------
#Completely removes a product from the system.
def delete_product(inventory,delete):
    if not delete in inventory:
        print("\033[91mThe product is not registered.\033[0m")
    else:
        print(f'\033[92mThe product "{inventory[delete]["product"]}" was deleted successfully.\033[0m')
        inventory.pop(delete)
#------------------------------------------------------------------------------------

quantity_discount = 3
percentage_discount = 0.1

def register_Sale(inventory, id_product):
    if not id_product in inventory:
        print("\033[91mThe product is not registered.\033[0m")
    else:
        try:
            customer = input("Enter customer: ").strip().lower()
            stock = int(input("Enter quantity to sell: "))

            while not customer:
                print("Customer name cannot be empty.")
                customer = input("Enter customer: ").strip().lower()
                stock = int(input("Enter quantity to sell: "))

            if stock <= 0:
                print("Quantity must be greater than 0.")
            elif stock > inventory[id_product]["stock"]:
                print("Not enough stock available.")
                return
            else:
                # Deduct sold stock
                inventory[id_product]["stock"] -= stock

                unit_price = inventory[id_product]["price"]
                total_gross = unit_price * stock

                apply_discount = ""
                if stock >= quantity_discount:
                    apply_discount = "yes"
                else:
                    apply_discount = "No"

                # Calculate discount only if applicable
                if apply_discount == "yes":
                    discount = total_gross * percentage_discount
                else:
                    discount = 0

                total_neto = total_gross - discount

                # Save the sale
                sale = {
                    "customer": customer,
                    "producto_id": id_product,
                    "stock": stock,
                    "fecha": datetime.now().strftime("%Y-%m-%d"),
                    "apply_discount": apply_discount,
                    "total_gross": total_gross,
                    "total_neto": total_neto
                }
                sales.append(sale)
                print("Sale registered successfully.")
        except ValueError:
            print("Error: Invalid data.")
#------------------------------------------------------------------------------------------
#Shows all registered sales
def show_sales(sales):

    if len(sales) == 0:
        print("No sales registered.")
    else:
        print("--- List of Registered Sales ---")
        for sale in sales:
            product = inventory[sale["producto_id"]]
            print(f"Customer: {sale['customer']} | Product: {product['product']} | "
                f"Quantity: {sale['stock']} | Date: {sale['fecha']} | "
                f"Discount: {sale['apply_discount']} | "
                f"Gross Income: {sale['total_gross']:.2f} | Net Income: {sale['total_neto']:.2f}")




inventory= {
    "123":{"author":"adrian","product":"arroz","price":1000,"stock":10, "category": "grain"},
    "456":{"author":"alesis","product":"papa","price":1500,"stock":50, "category": "vegetables"},
    "789":{"author":"alex","product":"azucar","price":2000,"stock":15, "category": "grain"},
    "987":{"author":"maria","product":"leche","price":2500,"stock":20, "category": "dairy"},
    "654":{"author":"kate","product":"panela","price":300,"stock":25, "category": "grain"},
}

sales= []
#------------------------------------------------------------------------------------
while True:
    print("\n\033[92m-----------------Inventory Management-------------\033[0m\n")
    print("\033[94mMAIN MENU.\033[0m\n")
    print("1- Register product.")
    print("2- Query product.")
    print("3- Update product.")
    print("4- Delete product.")
    print("5- Register sale.")
    print("6- Show sales.")
    print("7- Exit the program.\n")
    
    option = input("\033[93mEnter the number between 1 and 7, of the option you wish to perform: \033[0m")

    
    match option:
            case "1":
                print("\n\033[94mRegister product.\033[0m")
                product_Identifier= validate_Product()

                if product_Identifier not in inventory and product_Identifier != None :
                    register(inventory, product_Identifier)
                    

                elif product_Identifier in inventory:
                    print("\033[91mThe product is already registered.\033[0m")
                    
            case "2":
                print("\n\033[94mQuery product.\033[0m")
                consult_product = validate_Product()
                if consult_product!= None:
                    show_products(inventory,consult_product)
                    

            case "3":
                print("\n\033[94mUpdate product.\033[0m")
                update_product= validate_Product()
                if update_product!= None:
                    update_Products(inventory,update_product)

            case "4":
                print("\n\033[94mDelete product.\033[0m")
                delete= validate_Product()
                if delete != None:
                    delete_product(inventory,delete)

            case "5":
                print("\n\033[94mRegister sale.\033[0m")
                id_product= validate_Product()
                if id_product != None:
                    register_Sale(inventory,id_product)

            case "6":
                show_sales(sales)

            case "7":
                print("\n\033[94mThank you for using the program. \n"
                "See you soon\033[0m")
                break
        
            case _ :
                print("\n\033[91m Invalid option.\033[0m \n")
